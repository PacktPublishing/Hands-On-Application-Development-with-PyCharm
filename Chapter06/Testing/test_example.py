import unittest


class MyTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)

    def test_stringcase(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Bar'.isupper())


if __name__ == '__main__':
    unittest.main()
