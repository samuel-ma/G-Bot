import unittest

from pywalrus import Walrus


class TestWalrus(unittest.TestCase):

    def test_get_name(self):
        self.assertEqual("PyWalrus", Walrus().get_name())


if __name__ == "__main__":
    unittest.main()