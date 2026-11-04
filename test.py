import unittest
from main import divide_and_conquer_profit, linear_scan_profit


class MaxProfitTests(unittest.TestCase):
    def test_normal_profit(self):
        prices = [10, 7, 5, 8, 11, 9]
        expected = (6, 2, 4)
        self.assertEqual(divide_and_conquer_profit(prices), expected)
        self.assertEqual(linear_scan_profit(prices), expected)

    def test_decreasing_prices(self):
        prices = [9, 8, 7, 6]
        expected = (0, None, None)
        self.assertEqual(divide_and_conquer_profit(prices), expected)
        self.assertEqual(linear_scan_profit(prices), expected)

    def test_one_price(self):
        prices = [5]
        expected = (0, None, None)
        self.assertEqual(divide_and_conquer_profit(prices), expected)
        self.assertEqual(linear_scan_profit(prices), expected)

    def test_best_trade_at_end(self):
        prices = [5, 1, 4, 2, 8]
        expected = (7, 1, 4)
        self.assertEqual(divide_and_conquer_profit(prices), expected)
        self.assertEqual(linear_scan_profit(prices), expected)


if __name__ == "__main__":
    unittest.main()
