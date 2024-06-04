import unittest
from Db import Db


class MyTestCase(unittest.TestCase):
    def test_Db(self):
        database = Db()
        called = database.query("select 1")
        self.assertEqual(called, [(1,)])  # add assertion here


if __name__ == '__main__':
    unittest.main()
