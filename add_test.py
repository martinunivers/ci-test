import unittest
from add import add

class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 1), 3, "Should be 3")
        print(add(2, 1))
    

if __name__ == '__main__':
    unittest.main()
