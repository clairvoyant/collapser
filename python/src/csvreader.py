#!/usr/bin/env python


import gzip
import bz2
import csv


"""  is a wrapper class on top of csv, it reads gz, bz or csv files. 
     adn will call a callback for each read function.
"""



def parseCSV(files, cb, param):
    """ implement a csv reader reactor, the callback is executed per each csv record. """
    
    # TODO read gz and bz compresed csv files.

    for file in files:
        f = None

        if file.endswith(".gz"):
           f = gzip.open(file, "r")
        elif file.endswith(".bz2"):
           f = bz2.open(file, "r")
        else:
           f = open(file, "r")

        reader = csv.reader(f)

        for row in reader:
            cb(row, param)

        f.close()


