 
# tests/test_trade_executor.py

import unittest
from backtester.trade_executor import Portfolio

class TestTradeExecutor(unittest.TestCase):

    def test_not_enough_cash(self):
        portfolio = Portfolio(100)
        decision = {'action': 'buy', 'quantity': 2}
        price_data = {'close': 60, 'symbol': 'TEST', 'timestamp': '2021-01-01 09:30'}
        portfolio.execute_trade(decision, price_data)
        self.assertEqual(portfolio.cash, 100)
        self.assertEqual(portfolio.positions.get('TEST', 0), 0)

    def test_not_enough_holdings(self):
        portfolio = Portfolio(100000)
        decision = {'action': 'sell', 'quantity': 5}
        price_data = {'close': 100, 'symbol': 'TEST', 'timestamp': '2021-01-01 09:30'}
        portfolio.execute_trade(decision, price_data)
        self.assertEqual(portfolio.cash, 100000)
        self.assertEqual(portfolio.positions.get('TEST', 0), 0)

if __name__ == '__main__':
    unittest.main()
