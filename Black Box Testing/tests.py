# _____________________________________________________________________________
# Name:             Kristina Montanez
# Date:             1/24/2022
# Class:            CS 362
# Project:          1 - Writing Black Box Tests
# File:             tests.py
# Description:      Series of unit tests to test a function called
#                   credit_card_validator that is passed a sequence of digits
#                   as a string that represents a credit card number. This
#                   function will return True if it is a valid credit card
#                   number, otherwise, it will return False. Limits are: Visa
#                   Prefix(es): 4, Length: 16; MasterCard Prefix(es): 51
#                   through 55 and 2221 through 2720,Length: 16; American
#                   Express Prefix(es): 34 and 37, Length: 15. There are 6
#                   bugs in total.
# _____________________________________________________________________________
#   2)  MODULE IMPORTS
# ___________________________________
import unittest
from credit_card_validator import credit_card_validator


#   3)  PROJECT CODE
# ___________________________________
#
# Let's first start with error guessing. Below are my first shot guesses
# to see if I can't catch the errors through boundary issues that were
# discussed in the materials. I decided to cover three ways of
# partitioning the tests:
#
#   (1) Take care of edge cases
#
#   (2) Per Ed Discussion # 86 make a matrix that covered all three
#   requirements (length, prefix, and checksum) and edge cases that will
#   apply to each category. PLEASE NOTE THAT THIS ALSO FALLS UNDER PARTITION
#   METHOD; and
#
#   (3) create test cases for correct inputs.

class TestCase(unittest.TestCase):
    """
    A testing suite for testing the requirements for card numbers including
    Visa, Mastercard, and American Express. Tests will include true or false
    assertions.
    """
    # ___________________________________
    # Edge Cases:
    # ___________________________________
    def test_1(self):
        # tests to see if the card number is empty.
        # Using error guessing.
        self.assertFalse(credit_card_validator(""),
                         msg='result={}'.format(credit_card_validator(
                             "")))

    def test_2a(self):
        # tests to see if the card number is valid in all three
        # requirements but is a negative number (VISA).
        # Using error guessing.
        self.assertFalse(credit_card_validator("-4254163524896546"),
                         msg='result={}'.format(credit_card_validator(
                             "-4254163524896546")))

    def test_2b(self):
        # tests to see if the card number is valid in all three
        # requirements but is a negative number (MasterCard 51-55).
        # Using error guessing.
        self.assertFalse(credit_card_validator("-5154128641523651"),
                         msg='result={}'.format(credit_card_validator(
                             "-5154128641523651")))

    def test_2c(self):
        # tests to see if the card number is valid in all three
        # requirements but is a negative number (American Express 34).
        # Using error guessing.
        self.assertFalse(credit_card_validator("-345784126548653"),
                         msg='result={}'.format(credit_card_validator(
                             "-345784126548653")))

    def test_3a(self):
        # tests to see if the card number is all zeros (16 length).
        # Using error guessing.
        self.assertFalse(credit_card_validator("0000000000000000"),
                         msg='result={}'.format(credit_card_validator(
                             "0000000000000000")))

    def test_3b(self):
        # tests to see if the card number is all zeros (15 length).
        # Using error guessing.
        self.assertFalse(credit_card_validator("000000000000000"),
                         msg='result={}'.format(credit_card_validator(
                             "000000000000000")))

    def test_4a(self):
        # tests to see if the card number didn't enter (most likely
        # just a zero).
        # Using error guessing.
        self.assertFalse(credit_card_validator("0"),
                         msg='result={}'.format(credit_card_validator(
                             "0")))

    def test_4b(self):
        # tests to see if the card number didn't enter a valid prefix
        # but only one digit.
        # Using error guessing.
        self.assertFalse(credit_card_validator("4"),
                         msg='result={}'.format(credit_card_validator(
                             "4")))

    def test_5a(self):
        # tests to see if the card number doesn't have any requirement,
        # all three are missing-17 numbers.
        # Using error guessing.
        self.assertFalse(credit_card_validator("72541879456325478"),
                         msg='result={}'.format(credit_card_validator(
                             "72541879456325478")))

    def test_5b(self):
        # tests to see if the card number doesn't have any requirement,
        # all three are missing-14 numbers.
        # Using error guessing.
        self.assertFalse(credit_card_validator("84512546785412"),
                         msg='result={}'.format(credit_card_validator(
                             "84512546785412")))

    # ___________________________________
    # VISA
    # Matrix of all three options:
    # length, prefix, and checksum.
    # ___________________________________
    def test_visa_matrix_1(self):
        # tests to see if the card number is 1 digit lower in prefix,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("3154874521654893"),
                         msg='result={}'.format(credit_card_validator(
                             "3154874521654893")))

    def test_visa_matrix_2(self):
        # tests to see if the card number is 1 digit higher in prefix,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("5841254632578949"),
                         msg='result={}'.format(credit_card_validator(
                             "5841254632578949")))

    def test_visa_matrix_3(self):
        # tests to see if the card number is 1 digit lower,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("458712546897544"),
                         msg='result={}'.format(credit_card_validator(
                             "458712546897544")))

    def test_visa_matrix_4(self):
        # tests to see if the card number is 1 digit higher,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("45871254689754459"),
                         msg='result={}'.format(credit_card_validator(
                             "45871254689754459")))

    def test_visa_matrix_5(self):
        # tests to see if the card number is 1 digit lower in checksum,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("456841254689743"),
                         msg='result={}'.format(credit_card_validator(
                             "456841254689743")))

    def test_visa_matrix_6(self):
        # tests to see if the card number is 1 digit higher in checksum,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("456841254689745"),
                         msg='result={}'.format(credit_card_validator(
                             "456841254689745")))

    def test_visa_matrix_7(self):
        # tests to see if the card number has prefix and length wrong,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("354617854935643"),
                         msg='result={}'.format(credit_card_validator(
                             "354617854935643")))

    def test_visa_matrix_8(self):
        # tests to see if the card number has prefix and checksum wrong,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("3546178549356435"),
                         msg='result={}'.format(credit_card_validator(
                             "3546178549356435")))

    def test_visa_matrix_9(self):
        # tests to see if the card number has length and checksum wrong,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("48759615348679542"),
                         msg='result={}'.format(credit_card_validator(
                             "48759615348679542")))

    # ___________________________________
    # AMERICAN EXPRESS - 34
    # Matrix of all three options:
    # length, prefix, and checksum.
    # ___________________________________

    def test_am34_matrix_1(self):
        # tests to see if the card number is 1 digit lower in prefix,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("335849561258472"),
                         msg='result={}'.format(credit_card_validator(
                             "335849561258472")))

    def test_am34_matrix_2(self):
        # tests to see if the card number is 1 digit higher in prefix,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("356897456186450"),
                         msg='result={}'.format(credit_card_validator(
                             "356897456186450")))

    def test_am34_matrix_3(self):
        # tests to see if the card number is 1 digit lower,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("34658794521646"),
                         msg='result={}'.format(credit_card_validator(
                             "34658794521646")))

    def test_am34_matrix_4(self):
        # tests to see if the card number is 1 digit higher,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("3465879452164659"),
                         msg='result={}'.format(credit_card_validator(
                             "3465879452164659")))

    def test_am34_matrix_5(self):
        # tests to see if the card number is 1 digit lower in checksum,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("346587945216461"),
                         msg='result={}'.format(credit_card_validator(
                             "346587945216461")))

    def test_am34_matrix_6(self):
        # tests to see if the card number is 1 digit higher in checksum,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("346587945216463"),
                         msg='result={}'.format(credit_card_validator(
                             "346587945216463")))

    def test_am34_matrix_7(self):
        # tests to see if the card number has prefix and length wrong,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("3565879452164617"),
                         msg='result={}'.format(credit_card_validator(
                             "3565879452164617")))

    def test_am34_matrix_8(self):
        # tests to see if the card number has prefix and checksum wrong,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("356587945216467"),
                         msg='result={}'.format(credit_card_validator(
                             "356587945216467")))

    def test_am34_matrix_9(self):
        # tests to see if the card number has length and checksum wrong,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("3485642517896584"),
                         msg='result={}'.format(credit_card_validator(
                             "3485642517896584")))

    # ___________________________________
    # AMERICAN EXPRESS - 37
    # Matrix of all three options:
    # length, prefix, and checksum.
    # ___________________________________

    def test_am37_matrix_1(self):
        # tests to see if the card number is 1 digit lower in prefix,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("364857954612548"),
                         msg='result={}'.format(credit_card_validator(
                             "364857954612548")))

    def test_am37_matrix_2(self):
        # tests to see if the card number is 1 digit higher in prefix,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("381439758614589"),
                         msg='result={}'.format(credit_card_validator(
                             "381439758614589")))

    def test_am37_matrix_3(self):
        # tests to see if the card number is 1 digit lower,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("37456841256481"),
                         msg='result={}'.format(credit_card_validator(
                             "37456841256481")))

    def test_am37_matrix_4(self):
        # tests to see if the card number is 1 digit higher,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("3745684125648167"),
                         msg='result={}'.format(credit_card_validator(
                             "3745684125648167")))

    def test_am37_matrix_5(self):
        # tests to see if the card number is 1 digit lower in checksum,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("375198735642546"),
                         msg='result={}'.format(credit_card_validator(
                             "375198735642546")))

    def test_am37_matrix_6(self):
        # tests to see if the card number is 1 digit higher in checksum,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("375198735642548"),
                         msg='result={}'.format(credit_card_validator(
                             "375198735642548")))

    def test_am37_matrix_7(self):
        # tests to see if the card number has prefix and length wrong,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("3875964859713525"),
                         msg='result={}'.format(credit_card_validator(
                             "3775964859713525")))

    def test_am37_matrix_8(self):
        # tests to see if the card number has prefix and checksum wrong,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("387596485971352"),
                         msg='result={}'.format(credit_card_validator(
                             "377596485971352")))

    def test_am37_matrix_9(self):
        # tests to see if the card number has length and checksum wrong,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("377596485971352375"),
                         msg='result={}'.format(credit_card_validator(
                             "377596485971352375")))

    # ___________________________________
    # MASTERCARD - 51-55
    # Matrix of all three options:
    # length, prefix, and checksum.
    # ___________________________________

    def test_master5155_matrix_1(self):
        # tests to see if the card number is 1 digit lower in prefix,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("5047568951453257"),
                         msg='result={}'.format(credit_card_validator(
                             "5047568951453257")))

    def test_master5155_matrix_2(self):
        # tests to see if the card number is 1 digit higher in prefix,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("5641756894235614"),
                         msg='result={}'.format(credit_card_validator(
                             "5641756894235614")))

    def test_master5155_matrix_3(self):
        # tests to see if the card number is 1 digit lower,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("534865976251455"),
                         msg='result={}'.format(credit_card_validator(
                             "534865976251455")))

    def test_master5155_matrix_4(self):
        # tests to see if the card number is 1 digit higher,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("54568233568965253"),
                         msg='result={}'.format(credit_card_validator(
                             "54568233568965253")))

    def test_master5155_matrix_5(self):
        # tests to see if the card number is 1 digit lower in checksum,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("5577418529638525"),
                         msg='result={}'.format(credit_card_validator(
                             "5577418529638525")))

    def test_master5155_matrix_6(self):
        # tests to see if the card number is 1 digit higher in checksum,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("5577418529638527"),
                         msg='result={}'.format(credit_card_validator(
                             "5577418529638527")))

    def test_master5155_matrix_7(self):
        # tests to see if the card number has prefix and length wrong,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("568321654987321652"),
                         msg='result={}'.format(credit_card_validator(
                             "568321654987321652")))

    def test_master5155_matrix_8(self):
        # tests to see if the card number has prefix and checksum wrong,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("5078945612378944"),
                         msg='result={}'.format(credit_card_validator(
                             "5078945612378944")))

    def test_master5155_matrix_9(self):
        # tests to see if the card number has length and checksum wrong,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("51514632895745621"),
                         msg='result={}'.format(credit_card_validator(
                             "51514632895745621")))

    # ___________________________________
    # MASTERCARD - 2221-2720
    # Matrix of all three options:
    # length, prefix, and checksum.
    # ___________________________________

    def test_master2221_matrix_1(self):
        # tests to see if the card number is 1 digit lower in prefix,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("2220465785236519"),
                         msg='result={}'.format(credit_card_validator(
                             "2220465785236519")))

    def test_master2221_matrix_2(self):
        # tests to see if the card number is 1 digit higher in prefix,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("2721321852365471"),
                         msg='result={}'.format(credit_card_validator(
                             "2721321852365471")))

    def test_master2221_matrix_3(self):
        # tests to see if the card number is 1 digit lower,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("256812035409621"),
                         msg='result={}'.format(credit_card_validator(
                             "256812035409621")))

    def test_master2221_matrix_4(self):
        # tests to see if the card number is 1 digit higher,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("26851463205623015"),
                         msg='result={}'.format(credit_card_validator(
                             "26851463205623015")))

    def test_master2221_matrix_5(self):
        # tests to see if the card number is 1 digit lower in checksum,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("2224560238794158"),
                         msg='result={}'.format(credit_card_validator(
                             "2224560238794158")))

    def test_master2221_matrix_6(self):
        # tests to see if the card number is 1 digit higher in checksum,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("2224560238794150"),
                         msg='result={}'.format(credit_card_validator(
                             "2224560238794150")))

    def test_master2221_matrix_7(self):
        # tests to see if the card number has prefix and length wrong,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("222046358974561"),
                         msg='result={}'.format(credit_card_validator(
                             "222046358974561")))

    def test_master2221_matrix_8(self):
        # tests to see if the card number has prefix and checksum wrong,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("2725684103256988"),
                         msg='result={}'.format(credit_card_validator(
                             "2725684103256988")))

    def test_master2221_matrix_9(self):
        # tests to see if the card number has length and checksum wrong,
        # otherwise the number is valid.
        # Using error guessing.
        self.assertFalse(credit_card_validator("26551458792365821"),
                         msg='result={}'.format(credit_card_validator(
                             "26551458792365821")))

    # ___________________________________
    # WITHIN RANGE TESTING
    # Tests for each prefix that should
    # produce positive results.
    # ___________________________________

    def test_positives_1(self):
        # tests to see if the card numbers are correct for VISA.
        # Using Partition and Error Guessing.
        self.assertTrue(credit_card_validator("4518270452367416"),
                        msg='result={}'.format(credit_card_validator(
                            "4518270452367416")))
        self.assertTrue(credit_card_validator("4624915455784832"),
                        msg='result={}'.format(credit_card_validator(
                            "4624915455784832")))
        self.assertTrue(credit_card_validator("4150277883204673"),
                        msg='result={}'.format(credit_card_validator(
                            "4150277883204673")))
        self.assertTrue(credit_card_validator("4163244687746635"),
                        msg='result={}'.format(credit_card_validator(
                            "4163244687746635")))

    def test_positives_2a(self):
        # tests to see if the card numbers are correct for MASTERCARD 51-55.
        # Using Partition and Error Guessing.
        self.assertTrue(credit_card_validator("5574728645450447"),
                        msg='result={}'.format(credit_card_validator(
                            "5574728645450447")))
        self.assertTrue(credit_card_validator("5574235625688368"),
                        msg='result={}'.format(credit_card_validator(
                            "5574235625688368")))
        self.assertTrue(credit_card_validator("5372079700525663"),
                        msg='result={}'.format(credit_card_validator(
                            "5372079700525663")))
        self.assertTrue(credit_card_validator("5274060730421684"),
                        msg='result={}'.format(credit_card_validator(
                            "5274060730421684")))
        self.assertTrue(credit_card_validator("5104280890225735"),
                        msg='result={}'.format(credit_card_validator(
                            "5104280890225735")))

    def test_positives_2b(self):
        # tests to see if the card numbers are correct for MASTERCARD
        # 2221-2720.
        # Using Partition and Error Guessing.
        self.assertTrue(credit_card_validator("2221516879425613"),
                        msg='result={}'.format(credit_card_validator(
                            "2221516879425613")))
        self.assertTrue(credit_card_validator("2222516879425612"),
                        msg='result={}'.format(credit_card_validator(
                            "2222516879425612")))
        self.assertTrue(credit_card_validator("2322516879425611"),
                        msg='result={}'.format(credit_card_validator(
                            "2322516879425611")))
        self.assertTrue(credit_card_validator("2424516879425618"),
                        msg='result={}'.format(credit_card_validator(
                            "2424516879425618")))
        self.assertTrue(credit_card_validator("2567516879445613"),
                        msg='result={}'.format(credit_card_validator(
                            "2567516879445613")))
        self.assertTrue(credit_card_validator("2607516879347696"),
                        msg='result={}'.format(credit_card_validator(
                            "2607516879347696")))
        self.assertTrue(credit_card_validator("2720514879347669"),
                        msg='result={}'.format(credit_card_validator(
                            "2720514879347669")))

    def test_positives_3a(self):
        # tests to see if the card numbers are correct for AMERICAN 34.
        # Using Partition and Error Guessing.
        self.assertTrue(credit_card_validator("349744341240144"),
                        msg='result={}'.format(credit_card_validator(
                            "349744341240144")))
        self.assertTrue(credit_card_validator("340028325883064"),
                        msg='result={}'.format(credit_card_validator(
                            "340028325883064")))
        self.assertTrue(credit_card_validator("349662380713781"),
                        msg='result={}'.format(credit_card_validator(
                            "349662380713781")))
        self.assertTrue(credit_card_validator("349948583368436"),
                        msg='result={}'.format(credit_card_validator(
                            "349948583368436")))
        self.assertTrue(credit_card_validator("349878524280616"),
                        msg='result={}'.format(credit_card_validator(
                            "349878524280616")))
        self.assertTrue(credit_card_validator("348085235461540"),
                        msg='result={}'.format(credit_card_validator(
                            "348085235461540")))

    def test_positives_3b(self):
        # tests to see if the card numbers are correct for AMERICAN 37.
        # Using Partition and Error Guessing.
        self.assertTrue(credit_card_validator("370036824477208"),
                        msg='result={}'.format(credit_card_validator(
                            "370036824477208")))
        self.assertTrue(credit_card_validator("374037824377253"),
                        msg='result={}'.format(credit_card_validator(
                            "374037824377253")))
        self.assertTrue(credit_card_validator("376837824873245"),
                        msg='result={}'.format(credit_card_validator(
                            "376837824873245")))
        self.assertTrue(credit_card_validator("379837624833040"),
                        msg='result={}'.format(credit_card_validator(
                            "379837624833040")))
        self.assertTrue(credit_card_validator("371628625803167"),
                        msg='result={}'.format(credit_card_validator(
                            "371628625803167")))


if __name__ == '__main__':
    unittest.main()
