# _____________________________________________________________________________
# Name:             Kristina Montanez
# Date:             1/31/2022
# Class:            CS 362
# Project:          2 - Improving Coverage
# File:             tests.py
# Description:      Series of unit tests to test a function called
#                   contrived_func that is passed a numerical value
#                   and will test either true or false depending on the
#                   conditional statement, and must have a case for each
#                   combination of conditions. There must only be 7 test
#                   cases, and only one assert for each case. The cases
#                   must find C1 through C12, and contain no linting errors.
#
#                   Source Code Provided:   contrived_func.py
# _____________________________________________________________________________
#   2)  MODULE IMPORTS
# _____________________________________________________________________________
import unittest
from contrived_func import contrived_func as conf


#   3)  PROJECT CODE
# _____________________________________________________________________________
#
#   No:     Condition(s):                                       T/F
#
#   1       100 < x > 150                                       T
#   2       (x*5 < 361) AND (x/2 < 24) AND (x==6)               F
#   3       (x*5 < 361) AND (x/2 < 24) AND (x!=6)               T
#   4       (x < 75) AND (x / 8 < 10) AND (x ** x % 5 != 0)     T
#   5       (x > 75) AND (x / 8 =< 10) AND (x ** x % 5 == 0)    T
#   6       (x =< 75) AND (x / 8 > 10) AND (x ** x % 5 == 0)    T
#   7       (x =< 75) AND (x / 8 <= 10) AND (x ** x % 5 != 0)   F

class TestCase(unittest.TestCase):
    """
    A testing suite to meet 100% Branch and Condition Coverage for
    each condition found in contrived_func.py.
    """
    def test_1(self):
        # Condition 1-Return True more than 100 and less than 150.
        self.assertTrue(conf(103),
                        msg='result={}'.format(conf(103)))

    def test_2(self):
        # Condition 2-Return False if the value is 6.
        self.assertFalse(conf(6),
                         msg='result={}'.format(conf(6)))

    def test_3(self):
        # Condition 3-Return True if value is not 6, but still is
        # less than 361 when multiplied by 5, AND less than 24 when
        # divided by 2. Meaning less than 72.2 and less than 48, BUT
        # NOT 6.
        self.assertTrue(conf(33),
                        msg='result={}'.format(conf(33)))

    def test_4(self):
        # Condition 3-Return True if value is less than 75, less than
        # (x/8 < 10), but does not have zero remainder when (x ** x) / 5.
        # NOTE: I realized I needed one more (T of F) + (T) for the second
        # elif statement.
        self.assertTrue(conf(73),
                        msg='result={}'.format(conf(73)))

    def test_5(self):
        # Condition 3-Return True if value is more than 75, more than
        # (x/8 < 10), and has a zero remainder when (x ** x) / 5.
        # NOTE: must be less than 101, otherwise it will follow
        # Condition # 1 branch.
        self.assertTrue(conf(90),
                        msg='result={}'.format(conf(90)))

    def test_6(self):
        # Condition 4-Return True if value is less than 75, less than
        # (x/8 < 10), and has a zero remainder when (x ** x) / 5.
        # NOTE: must be more than 48, otherwise it will follow
        # Condition # 3 branch.
        self.assertTrue(conf(50),
                        msg='result={}'.format(conf(50)))

    def test_7(self):
        # Condition7-Return False if the value is higher than 75, less
        # than 80, but does not have zero remainder when (x ** x) / 5.
        self.assertFalse(conf(157),
                         msg='result={}'.format(conf(157)))


if __name__ == '__main__':
    unittest.main()
