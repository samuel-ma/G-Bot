import unittest

from pywalrus import Inbox


class TestInbox(unittest.TestCase):

    def test_class(self):
        self.assertTrue(isinstance(Inbox(), Inbox))


if __name__ == "__main__":
    unittest.main()
