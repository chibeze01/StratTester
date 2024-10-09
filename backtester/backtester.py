# backtester/backtester.py

import subprocess
import asyncio
import logging
from websockets import connect
import json
from contextlib import contextmanager
from backtester.data_loader import load_data
from backtester.trade_executor import Portfolio
from backtester.utils import setup_logging, log_exception
from backtester.config import STRATEGY_EXE_PATH, WEBSOCKET_URI, INITIAL_CAPITAL

@contextmanager
def start_strategy_process():
    logging.info("Starting strategy executable.")
    strategy_process = subprocess.Popen([STRATEGY_EXE_PATH])
    try:
        yield strategy_process
    finally:
        logging.info("Waiting for strategy process to exit.")
        try:
            strategy_process.wait(timeout=5)
            logging.info("Strategy process terminated gracefully.")
        except subprocess.TimeoutExpired:
            logging.warning("Strategy process did not terminate in time. Killing it.")
            strategy_process.kill()
            strategy_process.wait()
            logging.info("Strategy process killed.")


async def run_backtester():
    logging.info("Backtester started.")

    # Load historical data
    price_data_stream = load_data('data/historical_data.csv')
    if not price_data_stream:
        logging.error("No data to process. Exiting.")
        return

    portfolio = Portfolio(INITIAL_CAPITAL)

    try:
        async with connect(WEBSOCKET_URI) as websocket:
            for price_data in price_data_stream:
                logging.info(f"Processing data point: {price_data['timestamp']}")
                await websocket.send(json.dumps(price_data))
                decision = await websocket.recv()
                decision = json.loads(decision)
                portfolio.execute_trade(decision, price_data)
                await asyncio.sleep(0.01)
            
            # Send shutdown command
            await websocket.send('__shutdown__')
            logging.info("Sent shutdown command to strategy server.")
    except Exception as e:
        log_exception(e)
    finally:
        # Output final portfolio value
        final_value = portfolio.get_portfolio_value({})
        logging.info(f"Final portfolio value: {final_value}")

    logging.info("Backtester finished.")

def main():
    setup_logging('logs/backtester.log')
    try:
        with start_strategy_process():
            asyncio.run(run_backtester())
    except Exception as e:
        log_exception(e)
    finally:
        logging.info("Backtester program has exited.")

if __name__ == "__main__":
    main()
