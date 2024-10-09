 
# backtester/trade_executor.py

import logging

class Portfolio:
    def __init__(self, initial_capital):
        self.cash = initial_capital
        self.positions = {}
        self.trade_history = []

    def execute_trade(self, decision, price_data):
        action = decision.get('action')
        symbol = price_data.get('symbol', 'UNKNOWN')
        price = price_data['close']
        quantity = decision.get('quantity', 1)  # Default quantity

        if action == 'buy':
            cost = price * quantity
            if self.cash >= cost:
                self.cash -= cost
                self.positions[symbol] = self.positions.get(symbol, 0) + quantity
                self.trade_history.append({
                    'symbol': symbol,
                    'action': 'buy',
                    'quantity': quantity,
                    'price': price,
                    'timestamp': price_data['timestamp']
                })
                logging.info(f"Bought {quantity} of {symbol} at {price}")
            else:
                logging.warning("Not enough cash to execute buy order")
        elif action == 'sell':
            holding = self.positions.get(symbol, 0)
            if holding >= quantity:
                self.cash += price * quantity
                self.positions[symbol] -= quantity
                self.trade_history.append({
                    'symbol': symbol,
                    'action': 'sell',
                    'quantity': quantity,
                    'price': price,
                    'timestamp': price_data['timestamp']
                })
                logging.info(f"Sold {quantity} of {symbol} at {price}")
            else:
                logging.warning("Not enough holdings to execute sell order")
        else:
            logging.warning(f"Unknown action: {action}")

    def get_portfolio_value(self, current_prices):
        total_value = self.cash
        for symbol, quantity in self.positions.items():
            total_value += current_prices.get(symbol, 0) * quantity
        return total_value
