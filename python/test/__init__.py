#! -*- coding: utf-8 -*-

import os
import sys



sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), "src"))

print sys.path

def load_tests(loader, standard_tests, pattern):
    # top level directory cached on loader instance
    this_dir = os.path.dirname(__file__)
    package_tests = loader.discover(start_dir=this_dir, pattern=pattern)
    standard_tests.addTests(package_tests)
    return standard_tests
