import unittest
from unittest.mock import patch
import fun_with_collections.basic_list as basic


class MyTestCase(unittest.TestCase):
    @patch('fun_with_collections.basic_list.get_input', return_value='5')
    def test_make_list(self, input):
        self.assertEqual(basic.make_list(),[4, 67, 90])


if __name__ == '__main__':
    unittest.main()
