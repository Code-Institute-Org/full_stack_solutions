import unittest
from vending_machine import give_change


class TestVendingMachine(unittest.TestCase):
    """
    Define a class that inherits from unittest which is the unit testing model that ships with Python.
    """

    def test_return_change(self):
        """
        Method name has to start with test_ in order for it to run. The assertEqual method is inherited from unittest.
        :return:
        """
        coins = give_change(17)
        self.assertEqual(coins, [10, 05, 02], 'wrong change given')
        self.assertEqual(give_change(18), [10, 5, 2, 1], 'wrong change given')

    def test_multiple_same_coins(self):
        self.assertEqual(give_change(4), [2, 2])
