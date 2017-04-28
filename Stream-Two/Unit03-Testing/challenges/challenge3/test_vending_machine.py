import unittest
from vending_machine import give_change, give_item_and_change


class TestVendingMachine(unittest.TestCase):
    """
    Define a class that inherits from unittest which is the
    unit testing model that ships with Python.
    """

    def test_return_change(self):
        """
        Method name has to start with test_ in order for it to run.
        The assertEqual method is inherited from unittest.
        """
        self.assertEqual(give_change(.17), [.10, .05, .02])
        self.assertEqual(give_change(.18), [.10, .05, .02, .01])
        self.assertEqual(give_change(.04), [.02, .02])

    def test_multiple_same_coins(self):
        """test if change can be given in multiples of a coin
        """
        self.assertEqual(give_change(.40), [.20, .20])

    def test_unavailable_item(self):
        """if user asks for an item that's unavailable,
        they should not be given the item and their money should be returned.
        """
        # The use of the _ is a convention to denote a throwaway
        # variable name that is being deliberately ignored.
        item, change, _ = give_item_and_change('crisps', .50)
        self.assertIsNone(item)
        self.assertEqual(change, .50)

    def test_not_enough_money(self):
        """if user asks for an item but pays too little,
        they should not be given the item,
        and their money should be returned
        """
        item, change, _ = give_item_and_change('coke', .50)
        self.assertIsNone(item)
        self.assertEqual(change, .50)

    def test_correct_change(self):
        """if user asks for an item and pays too much
        they should get the correct change
        """
        item, change, _ = give_item_and_change('coke', 1.00)
        self.assertEqual(change, [.20, .05, .02])
