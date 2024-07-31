# Lab#7 - Whitebox testing
# SC353201 Software Quality Assurance
# Semester 1/2567
# Author 653380136-7 Paweennawat Sukruam

import unittest
import sys
sys.path.insert(0,'D:\SQA\SQA-2024\SQA-2024\Lab7\assignment\clumpCount\source')
from CountClump import CountClump

class test_CountClump(unittest.TestCase):
    def setUp(self):
        self.count = count.CountClump()
        self.nums = []
        testname = self.shortDescription()
    
    def tearDown(self):
        print('\nend of test', self.shortDescription())
        
    def test_add_two_number(self):
        """Add two numbers"""
        result = self.count.count_clumps(self.nums)
        self.assertEqual(result, 0)
