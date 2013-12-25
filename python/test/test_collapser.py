#!/usr/bin/python


import sys
import os
sys.path.insert(0, os.path.dirname("../lib/"))

import unittest
from libcollapser import *

test_onecolum = [
    [ "dummy", "1", "20", "dim1_0", "dim2_1"],
    [ "dummy", "2", "21", "dim2_0", "dim2_1"],
    [ "dummy", "3", "22", "dim1_0", "dim2_1"],
    [ "dummy", "4", "23", "dim2_0", "dim2_1"],
    [ "dummy", "5", "100", "dim1_0", "dim2_1"]
]

test_results1 = """dim1_0,9,142
dim2_0,6,44
"""

test_results2 = """dim1_0,dim2_1,9,142
dim2_0,dim2_1,6,44
"""
test_results3 = [ 
    ["dim1_0,dim2_1",9,142 ],
    ["dim2_0,dim2_1",6,44 ]
]


class TestCollapserSuite(unittest.TestCase):

    def setUp(self):
        return

    def test_onecolumn(self):
        col = Collapser()
        col.init([3], [1,2])
        for row in test_onecolum:
            col.do(row)
            
        self.assertEqual(str(col), test_results1)
            
    def test_twocolumn(self):
        col = Collapser()
        col.init([3,4], [1,2])
        for row in test_onecolum:
            col.do(row)
            
        self.assertEqual(str(col), test_results2)

    def test_iterator(self):
        col = Collapser()
        col.init([3,4], [1,2])
        for row in test_onecolum:
            col.do(row)
            
        for (row1, row2) in zip(iter(col), test_results3):
           self.assertEqual(row1, row2)
    



if __name__ == "__main__":
   unittest.main()
