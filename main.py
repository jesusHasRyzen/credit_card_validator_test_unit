import unittest
from credit_card_validator import credit_card_validator

class validate_creditCards(unittest.TestCase):
    pass
    def test1(self):
        cc = "111111111111111"
        self.assertFalse(credit_card_validator(cc))

    #visa
    def test2(self):
        cc ="4197394215553472"
        self.assertTrue(credit_card_validator(cc))
    def test3(self):
        cc = "412345678910002"
        self.assertFalse(credit_card_validator(cc))
    def test4(self):
        cc = "41234567891230005"
        self.assertFalse(credit_card_validator(cc))
    #mastercard
    def test5(self):
        cc = "5574841344560505"
        self.assertTrue(credit_card_validator(cc))
    def test6(self):
        cc = "5023456789120004"
        self.assertFalse(credit_card_validator(cc))
    def test7(self):
        cc = "5623456789120004"
        self.assertFalse(credit_card_validator(cc))
    def test8(self):
        cc = "2020456789120004"
        self.assertFalse(credit_card_validator(cc))
    def test9(self):
        cc = "2721456789120004"
        self.assertFalse(credit_card_validator(cc))
    #amex
    def test10(self):
        cc = "349785103358814"
        self.assertTrue(credit_card_validator(cc))
    def test11(self):
        cc = "332345678910009"
        self.assertFalse(credit_card_validator(cc))
    def test12(self):
        cc = "382345678910008"
        self.assertFalse(credit_card_validator(cc))
if __name__ == '__main__':
    unittest.main(verbosity = 2 )


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
