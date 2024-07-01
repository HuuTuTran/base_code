# test_my_module.py
import unittest
from my_module import add, subtract

class TestMyModule(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, -1), 0)

if __name__ == '__main__':
    unittest.main()