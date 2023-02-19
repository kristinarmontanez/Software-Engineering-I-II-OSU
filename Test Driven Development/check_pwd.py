# _____________________________________________________________________________
# Name:             Kristina Montanez
# Date:             2/14/2022
# Class:            CS 362
# Project:          A2 - TDD Hands On
# File:             check_pwd.py
# Description:      Function called check_pwd.py that check_pwd accepts a
#                   string and returns True if it meets the criteria listed
#                   below, otherwise it returns False. Criteria include range
#                   of 8-20 chars, one lowercase, one uppercase, one digit,
#                   one symbol from the list: "~`!@#$%^&*()_+-= ".
# _____________________________________________________________________________
#   1)  MODULE IMPORTS
# ______________________________________________
# Per instructions, we assume that
# only strings will be sent to the
# check_pwd.
import string

#   1)  CODE SOURCES
# ______________________________________________
#
#   NOTE:   sources are referenced below in the
#           code, e.g. "REF #1"
#
#   1.  example code from materials:
#       "Exploration: Test-Driven Development"
#
#   2.  Per Ed Discussion #185, start code with
#       "return True" first before creating test
#       code.
#
#   3.  GeeksforGeeks- "isupper(), islower(),
#       lower(), upper() in Python and their
#       applications".
#       https://www.geeksforgeeks.org/isupper-
#       islower-lower-upper-python-applications/
#
#   4.  GeeksforGeeks- "Python String isdigit()
#       Method".
#       https://www.geeksforgeeks.org/python-
#       string-isdigit-method/
#
#   5.  Programiz- "Python Program to Find
#       ASCII Value of Character."
#       https://www.programiz.com/python-
#       programming/examples/ascii-character
#       NOTE: Per Ed Discussion, non-list symbols
#       are not allowed.
#
#
#   3)  PROJECT CODE
# ______________________________________________


def check_pwd(pwd):
    # Variables to use:
    # __________________________________________
    password_length = len(pwd)
    lower_case = 0
    upper_case = 0
    has_digit = 0
    has_symbol = 0
    symbol_list = '~`!@#$%^&*()_+-='
    all_symbols = list(pwd)
    ascii_count = 0
    # __________________________________________
    #
    # "Must be between 8 and 20 characters (inclusive)"
    # First, make all passwords that fall outside this
    # range fail.
    if password_length < 8 or password_length > 20:
        return False

    # "Must contain at least one lowercase letter".
    # Next, make all passwords that do not have a
    # lowercase letter False. REF #3.
    for char in pwd:
            if char.islower():
                lower_case += 1
    if lower_case == 0:
        return False

    # "Must contain at least one uppercase letter".
    # Next, make all passwords that do not have a
    # uppercase letter False. REF #3.
    for char in pwd:
            if char.isupper():
                upper_case += 1
    if upper_case == 0:
        return False

    # "Must contain at least one digit".
    # Next, make all passwords that do not have a
    # digit False. REF #4.
    for char in pwd:
            if char.isdigit():
                has_digit += 1
    if has_digit == 0:
        return False

    # "Must contain at least one symbol from:"
    #   ~`!@#$%^&*()_+-=
    # Next, make all passwords that do not have a
    # symbol False.
    for char in pwd:
        for symbol in symbol_list:
            if char == symbol:
                has_symbol += 1
    if has_symbol == 0:
        return False

    # The listed symbols "are the only permitted
    # symbols". This means we need to filter out
    # all other symbols per REF #5.
    # Next, make all passwords that do not have a
    # symbol False. REF #5.
    for sym in all_symbols:
        # check if ascii meets the ascii of list
        # of correct symbols.
        for ascii in symbol_list:
            if ord(sym) == ord(ascii):
                ascii_count += 1
        # check if ascii is a digit.
        if (ord(sym) >= 48) and (ord(sym) <= 57):
            ascii_count += 1
        # check if ascii is a uppercase.
        if (ord(sym) >= 65) and (ord(sym) <= 90):
            ascii_count += 1
        # check if ascii is a lowercase.
        if (ord(sym) >= 97) and (ord(sym) <= 122):
            ascii_count += 1
    # After adding up all ascii numbers in string,
    # check if it's all allowed chars/symbols.
    if ascii_count != len(pwd):
        return False

    # If the code meets all requirements, return
    # True. All stipulations are filtered out
    # by this point.
    else:
        return True
