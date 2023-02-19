# _____________________________________________________________________________
# Name:             Kristina Montanez
# Date:             2/14/2022
# Class:            CS 362
# Project:          A2 - TDD Hands On
# File:             tests.py
# Description:      Series of unit tests to test a function called
#                   check_pwd.py that check_pwd accepts a string and returns
#                   True if it meets the criteria listed below, otherwise it
#                   returns False. Criteria include range of 8-20 chars, one
#                   lowercase, one uppercase, one digit, and one symbol
#                   from the list: "~`!@#$%^&*()_+-= ".
# _____________________________________________________________________________
#   1)  MODULE IMPORTS
# ______________________________________________
# Per instructions, we assume that
# only strings will be sent to the
# check_pwd.
import unittest
from unittest import TestCase
import string
from check_pwd import check_pwd

#   1)  CODE SOURCES
# ______________________________________________
#   1.  example code from materials:
#       "Exploration: Test-Driven Development"
#
#   3)  PROJECT CODE
# ______________________________________________


class TestCase(unittest.TestCase):
    """
    A testing suite for testing the requirements for check_pwd.py
    including range of 8-20 chars, one lowercase, one uppercase,
    one digit, and one symbol from the list: "~`!@#$%^&*()_+-= ".
    """
    def test1(self):
        # Per instructions, first test is written to see if
        # an empty string is rejected correctly. This is an
        # example already given.
        input = ""
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test2(self):
        # Check if password has 1 less than 8 characters,
        # otherwise, has all the requirements.
        input = "1Aa!abc"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test3(self):
        # Check if password has 1 more than 20 characters,
        # otherwise, has all the requirements.
        input = "0Aa@abcefgh12345*()+="
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test4(self):
        # Check if password has no lowercase characters,
        # otherwise, has all the requirements.
        input = "0@ABCDEF12345*"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test5(self):
        # Check if password has 1 lowercase character,
        # and has all the requirements.
        input = "0@aBCDEF12345*"
        expected = True
        self.assertEqual(check_pwd(input), expected)

    def test6(self):
        # Check if password has no uppercase characters,
        # otherwise has all the requirements.
        input = "0@abcdef12345*"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test7(self):
        # Check if password has 1 uppercase characters,
        # otherwise has all the requirements.
        input = "0@Abcdef12345*"
        expected = True
        self.assertEqual(check_pwd(input), expected)

    def test8(self):
        # Check if password has lower and uppercase
        # characters, correct length, and a symbol,
        # but no digits.
        input = "@AbcdefHijk*"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test9(self):
        # Check if password has lower and uppercase
        # characters, correct length, and a symbol,
        # and 1 digit.
        input = "@A2cdefHijk*"
        expected = True
        self.assertEqual(check_pwd(input), expected)

    def test10(self):
        # Check if password has lower and uppercase
        # characters, correct length, and a digit,
        # but no symbol.
        input = "ABC2cdefHijk"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test11(self):
        # Check if password has lower and uppercase
        # characters, correct length, and a digit,
        # and one correct symbol, but also an
        # incorrect symbol.
        input = "@ABC2cdefHij<"
        expected = False
        self.assertEqual(check_pwd(input), expected)


if __name__ == '__main__':
    unittest.main()



