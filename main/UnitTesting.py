import unittest


class UnitTesting(unittest.TestCase):


    # Returns True or False.
    def test(self):
        self.assertTrue(True)

    def test_checkCase(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_checkCase2(self):
        self.assertTrue('foo'.isupper()) # error happened


if __name__ == '__main__':
    unittest.main()