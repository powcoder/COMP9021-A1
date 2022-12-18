https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
import unittest
from unittest.mock import patch
from collections import OrderedDict
import roman_arabic as roman

data = OrderedDict()


class Total_test(unittest.TestCase):

    def test_roman(self):
        for i in data:
            input_test = [i]
            with patch('builtins.input', side_effect=input_test):
                with patch('builtins.print', side_effect=print) as mock:
                    roman.please_convert()
                    mock.assert_called_once_with(data[i])
                    data[i] = 'Success'


if __name__ == '__main__':
    with open('test.txt') as file:
        test_data = file.readlines()
        for i in range(0, len(test_data), 2):
            data[test_data[i][:-1]] = test_data[i + 1][:-1]
    try:
        unittest.main()
    except:
        for i in data:
            if data[i] != 'Success':
                print('You fail this case :', i)
                break
