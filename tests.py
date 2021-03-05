import random
import datetime
import unittest
from task import conv_num
from task import my_datetime

class TestCase(unittest.TestCase):
    # check if empty argument returns None for function 1
    def test1(self):
        num = ''
        self.assertEqual(conv_num(num), None,
                         msg='f1 empty str not none={}'.format(num))

    # check var type not str returns None for function 1
    def test2(self):
        num = 456
        self.assertEqual(conv_num(num), None,
                         msg='f1 non-str type not none={}'.format(num))

    # check hex with incorrect prefix format returns None for function 1
    def test3(self):
        num = '0X9B'
        self.assertEqual(conv_num(num), None,
                         msg='f1 bad hex format not none={}'.format(num))

    # check hex with no numbers after prefix returns None for function 1
    def test4(self):
        num = '0x'
        self.assertEqual(conv_num(num), None,
                         msg='f1 empty hex type not none={}'.format(num))

    # check string with only - sign returns None for function 1
    def test5(self):
        num = '-'
        self.assertEqual(conv_num(num), None,
                         msg='f1 only neg sign not none={}'.format(num))

    # check that neg zero returns zero as float for function 1
    def test6(self):
        num = '-0.0'
        self.assertEqual(conv_num(num), 0.0,
                         msg='f1 incorrect -0.0 !={}'.format(num))

    # check that neg num with space btw num and sign returns None function 1
    def test7(self):
        num = '- 45.7'
        self.assertEqual(conv_num(num), None,
                         msg='f1 {} not none'.format(num))

    # check that neg num with multi decimal returns None function 1
    def test8(self):
        num = '-12.900.88'
        self.assertEqual(conv_num(num), None,
                         msg='f1 {} multi decimal not none'.format(num))

    # check hex with decimal point returns None function 1
    def test9(self):
        num = '0xbd.a'
        self.assertEqual(conv_num(num), None,
                         msg='f1 hex w/ decimal not none={}'.format(num))

    # check hex with invalid alphabet letter returns None function 1
    def test10(self):
        num = '0x0Z0'
        self.assertEqual(conv_num(num), None,
                         msg='f1 invalid hex letter not None = {}'.format(num))

    # check that float with non-number returns None function 1
    def test11(self):
        num = '43.0k5'
        self.assertEqual(conv_num(num), None,
                         msg='f1 float with non-num not None = {}'.format(num))

    # check valid string int with leading zeros returns int function 1
    def test12(self):
        num = '-045'
        self.assertEqual(conv_num(num), -45,
                         msg='f1 valid int with lead zeros '
                             'not valid = {}'.format(num))

    # check successive decimals for number returns None
    def test13(self):
        num = '..69420'
        self.assertEqual(conv_num(num), None,
                         msg='f1 successive decimals not None = '
                             '{}'.format(num))

    # check decimals at both ends of float returns None
    def test14(self):
        num = '.9339.'
        self.assertEqual(conv_num(num), None,
                         msg='f1 decimals at both ends not None = '
                             '{}'.format(num))

    # check consecutive ending decimals returns None
    def test15(self):
        num = '-35...'
        self.assertEqual(conv_num(num), None, msg='f1 trailing decimals '
                                                  'not None = {}'.format(num))

    # Generate 100 random test cases to verify function 2
    def test16(self):
        tests_to_generate = 100

        # Generate random test cases
        for i in range(tests_to_generate):
            # Generate test time
            seconds = random.randint(0,9999999999)
            output = my_datetime(seconds)
            date = datetime.datetime.utcfromtimestamp(seconds)
            expected = date.strftime('%m-%d-%Y')
            # Generate failure message if my_datetime doesn't match expectation
            if output != expected:
                print('Failure: {} should be {}'.format(output, expected))

    #check if decimal 954786 converts to hex number corectly in big endian fashion
    def test17(self):
        num = 954786
        self.assertEqual(conv_endian(num, 'big'), '0E 91 A2')

    #check if the function with no second argument gives the same result as test17
    def test18(self):
        num = 954786
        self.assertEqual(conv_endian(num), '0E 91 A2')

    #check if negative decimal gives the right result
    def test19(self):
        num = -954786
        self.assertEqual(conv_endian(num), '-0E 91 A2')

    #check if little endian works correcly
    def test20(self):
        num = 954786
        self.assertEqual(conv_endian(num, 'little'), 'A2 91 0E')

    #check if negative decimal and little endian work togther correcly 
    def test21(self):
        num = -954786
        self.assertEqual(conv_endian(num, 'little'), '-A2 91 0E')

    #check if 'endian='little' argument works as supposed to 
    def test22(self):
        num = -954786
        self.assertEqual(conv_endian(num, endian='little'), '-A2 91 0E')

    #check if the case when endian argument is incorrect gives the correct result
    def test22(self):
        num = -954786
        self.assertEqual(conv_endian(num, endian='small'), 'None')

    #check if the decimal 4325 gives the correct result
    def test23(self):
        num = 4325
        self.assertEqual(conv_endian(num), '10 E5')

    #check if the decimal -4325 gives the correct result
    def test24(self):
        num = 4325
        self.assertEqual(conv_endian(num, 'little'), 'E5 10')

if __name__ == '__main__':
  unittest.main()