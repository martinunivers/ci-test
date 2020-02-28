import unittest
from add import add

class Test(unittest.TestCase):
  def add_test(self):
    self.assertEqual(add(2, 1), 3, "Should be 3")
    
if __name__ == "__main__":
  unittest.main()
