import unittest

from pywalrus import Message


class TestMessage(unittest.TestCase):

    def test_class(self):
        self.assertTrue(isinstance(Message(), Message))


if __name__ == "__main__":
    unittest.main()
