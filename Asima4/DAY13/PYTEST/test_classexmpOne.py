import unittest

class TestExampleOne(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\nSetup class method called (unittest)')
        cls.test_data = [
            {'a': 2, 'b': 3, 'expected_sum': 5},
            {'a': 10, 'b': 5, 'expected_sum': 15},
            {'a': -1, 'b': 1, 'expected_sum': 0}
        ]

    @classmethod
    def tearDownClass(cls):
        print('\nTeardown class method called (unittest)')
        cls.test_data = None 

    def setUp(self):
        print('\nSetup method called (unittest)')

    def tearDown(self):
        print('\nTeardown method called (unittest)')

    def test_add(self):
        print('\nAdd method called (unittest)')
        for data_item in self.test_data:
            a = data_item['a']
            b = data_item['b']
            expected_sum = data_item['expected_sum']
            with self.subTest(msg=f"Testing {a} + {b}"): 
                self.assertEqual(a + b, expected_sum, f"Expected {a} + {b} to be {expected_sum}")

    def test_sub(self):
        print('\nSub method called (unittest)')
        self.assertEqual(8 - 3, 5, "Expected 8 - 3 to be 5")
        self.assertEqual(10 - 2, 8, "Expected 10 - 2 to be 8")

if __name__ == '__main__':
    unittest.main()