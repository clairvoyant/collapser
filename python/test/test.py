#!/usr/bin/env python
"""
Created on Wed Dec 25 14:22:52 2013

@author: jrubio
"""


import sys, os, re
import unittest

base_path = os.path.dirname(os.path.dirname(__file__))

TESTED_CODE = os.path.join(base_path,"src")  # Path to tested code.
TEST_CODE   = os.path.join(base_path,"test") # Path to test code.

sys.path.append(TESTED_CODE)
sys.path.append(TEST_CODE)

# Import all the tests from 'test/'.
for testFile in os.listdir(TEST_CODE):
    if re.match("^test_.+\.py$", testFile):
        exec "from %s import *" % testFile[0:-3]

# Run the tests.
if __name__ == "__main__":
    unittest.main()
