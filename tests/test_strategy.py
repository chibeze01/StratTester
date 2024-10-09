 
# tests/test_strategy.py

import unittest
from strategy.strategy_logic import make_decision

class TestStrategy(unittest.TestCase):

    def test_make_decision_buy(self):
        price_data = {'close': 105, 'timestamp': '2021-01-01 00:00:00'}
        decision = make_decision(price_data)
        self.assertEqual(decision['action'], 'buy')

    def test_make_decision_sell(self):
        price_data = {'close': 95, 'timestamp': '2021-01-01 00:00:00'}
        decision = make_decision(price_data)
        self.assertEqual(decision['action'], 'sell')

if __name__ == '__main__':
    unittest.main()
