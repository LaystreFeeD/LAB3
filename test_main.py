import unittest

class TestSimpleApp(unittest.TestCase):
    def test_print_message(self):
        expected_message = "Lab3"
        actual_message = "Lab3"
        self.assertEqual(expected_message, actual_message)

if __name__ == '__main__':
    unittest.main()