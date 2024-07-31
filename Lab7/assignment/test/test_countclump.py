# Lab#7 - Whitebox testing
# SC353201 Software Quality Assurance
# Semester 1/2567
# Author 653380136-7 Paweennawat Sukruam

import unittest
import sys
sys.path.insert(0,'/workspaces/Lab7_653380136-7/Lab7/assignment/clumpCount/source')
from CountClump import CountClump

class test_CountClump_C_DC(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Start testing class CountClump.")

    @classmethod
    def tearDownClass(cls):
        print('\nFinish testing class CountClump.')

    def setUp(self):
        self.count = CountClump()
        testname = self.shortDescription()
        if testname == "nums is None":
            self.nums = []
            print("\n"+testname+"\n", self.nums)

        if testname == "len(nums) is 0":
            self.nums = ""
            print("\n"+testname+"\n", self.nums)

        if testname == "All condition in loop":
            self.nums = [1,1,2,2,2,3,4]
            print("\n"+testname+"\n", self.nums)
    
    def tearDown(self):
        print('\nend of test', self.shortDescription())
        
    def test_None(self):
        """nums is None"""
        result = self.count.count_clumps(self.nums)
        self.assertEqual(result, 0)

    def test_len_0(self):
        """len(nums) is 0"""
        result = self.count.count_clumps(self.nums)
        self.assertEqual(result, 0)

    def test_complete_loop(self):
        """All condition in loop"""
        result = self.count.count_clumps(self.nums)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
