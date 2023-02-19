# _____________________________________________________________________________
# Name:             Kristina Montanez
# Date:             2/7/2022
# Class:            CS 362
# Project:          3 - Random Testing Hands On
# File:             tests.py
# Description:      Series of random unit tests to test a function called
#                   credit_card_validator that is passed a sequence of digits
#                   as a string that represents a credit card number. This
#                   function will return True if it is a valid credit card
#                   number, otherwise, it will return False. Limits are the
#                   same as assignment for HW1. There are 5 bugs in total.
# _____________________________________________________________________________
#   1)  MODULE IMPORTS
# ___________________________________
import unittest
import random
from credit_card_validator import credit_card_validator

#   1)  CODE SOURCES
# ___________________________________
# 1. example code from materials: "Exploration: Random Testing."
#
#   3)  PROJECT CODE
# ___________________________________
#
# Let's first start with correct ranges, then ranges for each length
# of cc number. Below are my first shot guesses to see if I can't
# catch the errors through general boundaries without using any
# prefixes.
#
#   (1) First, I tested all correct and incorrect length ranges, which will
#   include lengths of 15
#       and 16 digits, from 3 prefix to 5 prefix.
#
#   (2) Test the correct length ranges only, which include all the
#       15-digit lengths, and all the 16-digit lengths.
#
#   (3) Test the "next-to" correct length ranges only, which include all
#       14-digit lengths, and all the 17-digit lengths. This range is
#       repeated from my HW1 assignment testing.


class TestCase(unittest.TestCase):
    """
    A testing suite for testing the requirements for card numbers including
    Visa, Mastercard, and American Express. Tests will include true or false
    assertions. The tests in this assignment, however, are randomly
    generated to catch new errors.
    """
    def test_visa(self):
        # First, test for the correct range and prefix for Visa, which is
        # 16 digits and starts with 4.
        for i in range(0, 50000):
            val = str(random.randint(4000000000000000, 4999999999999999))
            credit_card_validator(val)

    def test_mastercard_1(self):
        # Next, test for the correct range and prefix for MasterCard, which is
        # 16 digits and starts with 51 through 55.
        for i in range(0, 50000):
            val = str(random.randint(5100000000000000, 5599999999999999))
            credit_card_validator(val)

    def test_mastercard_2(self):
        # Next, test for the correct range and prefix for MasterCard, which is
        # 16 digits and starts with 2221 through 2720.
        for i in range(0, 50000):
            val = str(random.randint(2221000000000000, 2720999999999999))
            credit_card_validator(val)

    def test_americanx_1(self):
        # Next, test for the correct range and prefix for American Express,
        # which is 15 digits and starts with 34. Since this is a narrow range,
        # we will not need to test for a large number.
        for i in range(0, 10000):
            val = str(random.randint(340000000000000, 349999999999999))
            credit_card_validator(val)

    def test_americanx_2(self):
        # Next, test for the correct range and prefix for American Express,
        # which is 15 digits and starts with 37. Since this is a narrow range,
        # we will not need to test for a large number.
        for i in range(0, 10000):
            val = str(random.randint(370000000000000, 379999999999999))
            credit_card_validator(val)

    def test_15_length_all(self):
        # Next, check for all digits that will fit American Express length.
        # We do not need a large test pool here.
        for i in range(0, 500):
            val = str(random.randint(100000000000000, 999999999999999))
            credit_card_validator(val)

    def test_16_length_all(self):
        # Next, check for all digits that will fit Visa and MasterCard length.
        # We do not need a large test pool here, as it is partially
        # overlapping with other tests above.
        for i in range(0, 100):
            val = str(random.randint(1000000000000000, 9999999999999999))
            credit_card_validator(val)

    def test_14_length_all(self):
        # Next, check for all digits that will catch the shortest length -1.
        # For this test, I left the first boundary to include zero and
        # up, just in case as HW1 had an error that included a blank space.
        # We do not need a large test pool here.
        for i in range(0, 100):
            val = str(random.randint(0000000000, 9999999999))
            credit_card_validator(val)

    def test_17_length(self):
        # Next, check for all digits that will catch the shortest length +1.
        # We do not need a large test pool here.
        for i in range(0, 100):
            val = str(random.randint(10000000000000000, 99999999999999999))
            credit_card_validator(val)


if __name__ == '__main__':
    unittest.main()
