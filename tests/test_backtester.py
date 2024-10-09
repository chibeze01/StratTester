 
# tests/test_backtester.py

import unittest
from backtester.trade_executor import Portfolio

class TestBacktester(unittest.TestCase):

    def test_portfolio_initialization(self):
        portfolio = Portfolio(100000)
        self.assertEqual(portfolio.cash, 100000)
        self.assertEqual(portfolio.positions, {})

    def test_execute_buy_trade(self):
        portfolio = Portfolio(100000)
        decision = {'action': 'buy', 'quantity': 10}
        price_data = {'close': 100, 'symbol': 'TEST', 'timestamp': '2021-01-01 09:30'}
        portfolio.execute_trade(decision, price_data)
        self.assertEqual(portfolio.cash, 99000)
        self.assertEqual(portfolio.positions['TEST'], 10)

    def test_execute_sell_trade(self):
        portfolio = Portfolio(100000)
        portfolio.positions['TEST'] = 10
        decision = {'action': 'sell', 'quantity': 5}
        price_data = {'close': 100, 'symbol': 'TEST', 'timestamp': '2021-01-01 09:30'}
        portfolio.execute_trade(decision, price_data)
        self.assertEqual(portfolio.cash, 100500)
        self.assertEqual(portfolio.positions['TEST'], 5)

if __name__ == '__main__':
    unittest.main()
