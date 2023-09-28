import math
import unittest

def test_check(x):
    return x >= 50
    

class mytest(unittest.TestCase):
    def test(self):
        self.assertTrue(test_check(49))
        print("Passed")

if __name__=="__main__":
    unittest.main()