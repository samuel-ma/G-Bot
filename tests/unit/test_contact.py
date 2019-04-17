import unittest

from pywalrus import Contact


class TestContact(unittest.TestCase):

    def test_class(self):
        self.assertTrue(isinstance(Contact(), Contact))


if __name__ == "__main__":
    unittest.main()
