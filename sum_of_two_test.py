import unittest
from sum_of_two import *

class TestSumOfTwo(unittest.TestCase):
    def test_normal_true_case(self):
        a = [1,2,3]
        b = [6,7,8]
        v = 11
        self.assertEqual(sumOfTwo(a,b,v),True)
        
    def test_normal_false_case(self):
        a = [1,2,3]
        b = [6,7,8]
        v = 12
        self.assertEqual(sumOfTwo(a,b,v),False)
        
    def test_edge_true_case(self):
        a = [0]
        b = [0]
        v = 0
        self.assertEqual(sumOfTwo(a,b,v),True)
        
    def test_edge_false_case3(self):
        a = [0]
        b = [0]
        v = 1
        self.assertEqual(sumOfTwo(a,b,v),False)
        
    def test_edge_false_case1(self):
        a = []
        b = [6,7,8]
        v = 8
        self.assertEqual(sumOfTwo(a,b,v),False)
        
    def test_edge_false_case2(self):
        a = [1,2,3]
        b = []
        v = 3
        self.assertEqual(sumOfTwo(a,b,v),False)
        
    def test_mega_true(self):
        a = [i for i in range(10000)]
        b = [i for i in range(10000)]
        v = 20000
        self.assertEqual(sumOfTwo(a,b,v),False)
        
if __name__ == "__main__":
    unittest.main()
