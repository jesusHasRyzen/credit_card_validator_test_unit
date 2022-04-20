# Jesus Ponce
# April 19
# CS 362_400
import unittest
from credit_card_validator import credit_card_validator


class validate_creditCards(unittest.TestCase):
    pass

    # verifies invalid prefix, length, and check digit
    # returns false
    def test1(self):
        cc = "111111111111111"
        self.assertFalse(credit_card_validator(cc))

    # verifies for invalid input, no input
    # returns false
    def test2(self):
        cc = ""
        self.assertFalse(credit_card_validator(cc))

    # visa
    # verifies valid visa cc with correct prefix, length and check digit
    # returns true
    def test3(self):
        cc = "4197394215553472"
        self.assertTrue(credit_card_validator(cc))

    # verifies visa cc invalid due to incorrect check digit
    # returns false
    def test4(self):
        cc = "4197394215553470"
        self.assertFalse(credit_card_validator(cc))

    # verifies invalid visa cc, length too short for visa cc < 16
    # returns false
    # Boundary value testing
    def test5(self):
        cc = "412345678910002"
        self.assertFalse(credit_card_validator(cc))

    # verifies invalid visa cc, length too long for visa cc, > 16
    # returns false
    # Boundary value testing
    def test6(self):
        cc = "41234567891230005"
        self.assertFalse(credit_card_validator(cc))

    #  verifies invalid visa cc, due to incorrect prefix 5, not 4
    # returns false
    def test7(self):
        cc = "5197394215553472"
        self.assertFalse(credit_card_validator(cc))

    #  verifies invalid visa cc, due to incorrect prefix 3, not 4
    # returns false
    def test8(self):
        cc = "3197394215553472"
        self.assertFalse(credit_card_validator(cc))

    # mastercard
    # verifies valid mastercard cc with valid prefix, length, start with 55
    # returns true
    def test9(self):
        cc = "5574841344560505"
        self.assertTrue(credit_card_validator(cc))

    # verifies valid mastercard cc with valid prefix, length, start with 53
    # returns true
    def test10(self):
        cc = "5372076822583364"
        self.assertTrue(credit_card_validator(cc))

    # verifies valid mastercard cc with valid prefix, length, start with 51
    # returns true
    def test28(self):
        cc = "5121456789100051"
        self.assertTrue(credit_card_validator(cc))

    # verifies valid mastercard cc with valid prefix,length, start with 2221
    # return true
    def test29(self):
        cc = "2221456789100024"
        self.assertTrue(credit_card_validator(cc))

    # verifies valid mastercard cc with valid prefix,length, start with 2720
    # returns true
    def test30(self):
        cc = "2720456789100079"
        self.assertTrue(credit_card_validator(cc))

    # verifies invalid mastercard cc due to incorrect check digit
    # returns false
    def test11(self):
        cc = "5372076822583361"
        self.assertFalse(credit_card_validator(cc))

    # verifies invalid mastercard cc due to prefix below 51, range 51-55 or 2221-2720
    # returns false
    # Boundary value testing
    def test12(self):
        cc = "5023456789100001"
        self.assertFalse(credit_card_validator(cc))

    # verifies invalid mastercard cc due to prefix below 51, range 51-55 or 2221-2720
    # returns false
    # Boundary value testing
    def test13(self):
        cc = "5623456789100005"
        self.assertFalse(credit_card_validator(cc))

    # verifies invalid mastercard cc due to prefix below 51, range 51-55 or 2221-2720
    # returns false
    # Boundary value testing
    def test14(self):
        cc = "2220456789100033"
        self.assertFalse(credit_card_validator(cc))

    # verifies invalid mastercard cc due to prefix below 51, range 51-55 or 2221-2720
    # returns false
    # Boundary value testing
    def test15(self):
        cc = "2721456789100011"
        self.assertFalse(credit_card_validator(cc))

    # verifies invalid length for mastercard cc, length must be 16 not 17
    # returns false
    def test16(self):
        cc = "55748413445605050"
        self.assertFalse(credit_card_validator(cc))

    # def test17(self):
    #     cc = "5574841344560505"
    #     self.assertFalse(credit_card_validator(cc))
    # verifies invalid length for mastercard cc, length must be 16 not 15
    # returns false
    def test18(self):
        cc = "557484134456050"
        self.assertFalse(credit_card_validator(cc))

    # amex
    # verifies valid amex cc card with valid prefix, length, begin with 34
    # returns true
    def test19(self):
        cc = "349785103358814"
        self.assertTrue(credit_card_validator(cc))

    # verifies valid amex cc card with valid prefix, length, begin with 37
    # returns true
    def test20(self):
        cc = "370024503870802"
        self.assertTrue(credit_card_validator(cc))

    # verifies invalid amex cc due to incorrect check digit
    # returns false
    def test21(self):
        cc = "370024503870802"
        self.assertFalse(credit_card_validator(cc))

    # verifies invalid range for amex cc prefix, only 34 or 37 valid
    # returns false
    def test22(self):
        cc = "332345678910009"
        self.assertFalse(credit_card_validator(cc))

    # verifies invalid range for amex cc prefix, only 34 or 37 valid
    # returns false
    def test23(self):
        cc = "382345678910008"
        self.assertFalse(credit_card_validator(cc))

    # verifies invalid length for amex cc, too long, length must be 15 not 16,
    # with prefix 34 : returns false
    # Boundary value testing
    def test24(self):
        cc = "3497851033588141"
        self.assertFalse(credit_card_validator(cc))

    # verifies invalid length for amex cc, too short, length must be 15 not 14,
    # with prefix 34 : returns false
    # Boundary value testing
    def test25(self):
        cc = "34978510335881"
        self.assertFalse(credit_card_validator(cc))

    # verifies invalid length for amex cc, too long, length must be 15 not 16,
    # with prefix 37 : returns false
    # Boundary value testing
    def test26(self):
        cc = "3700245038708020"
        self.assertFalse(credit_card_validator(cc))

    # verifies invalid length for amex cc, too short, length must be 15 not 14,
    # with prefix 37 : returns false
    # Boundary value testing
    def test27(self):
        cc = "37002450387080"
        self.assertFalse(credit_card_validator(cc))


if __name__ == '__main__':
    unittest.main(verbosity=2)
