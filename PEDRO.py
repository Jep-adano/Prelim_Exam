import unittest

def equal():
    x = 'PEDRO'
    return x

class mytest(unittest.TestCase):

    def test(self):
        self.assertEqual(equal(), 'PEDRO')

if __name__=="__main__":
    unittest.main()
