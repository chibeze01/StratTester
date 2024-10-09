import asyncio
import websockets
import json
import logging
from strategy.strategy_logic import make_decision
from strategy.utils import setup_logging, log_exception

shutdown_event = asyncio.Event()  # Create an event to signal shutdown

async def process_data(websocket, path):
    try:
        async for message in websocket:
            if message == '__shutdown__':
                logging.info("Received exit command. Closing connection.")
                await websocket.close()
                shutdown_event.set()  # Signal the main function to shut down the server
                break
            price_data = json.loads(message)
            decision = make_decision(price_data)
            await websocket.send(json.dumps(decision))
    except Exception as e:
        log_exception(e)
        # Optionally close the connection
        await websocket.close()
    finally:
        logging.info("Connection closed.")

async def main():
    setup_logging()
    server = None
    try:
        server = await websockets.serve(process_data, 'localhost', 8765)
        logging.info("Strategy server started.")
        
        # Wait until the shutdown event is set
        await shutdown_event.wait()
    except Exception as e:
        log_exception(e)
    finally:
        logging.info("Strategy server shutting down.")
        if server:
            server.close()
            await server.wait_closed()
        logging.info("Strategy server has shut down.")

if __name__ == "__main__":
    asyncio.run(main())
