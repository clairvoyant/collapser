#!/usr/bin/env python

"""  is a class that takes a csv file as input and perform aritmetic operations in the
    columns. 

    The output will be the diferent rows colapsed into the key fields. 
"""

import sys
import getopt
import csv


from libcollapser import *
from csvreader import *

OPT_METRIC = 'metric='
OPT_DIM    = 'dim='
OPT_FILES  = "files="
OPT_HELP  = "help"

#######
# TODO
#
# TODO: use glob for file matching
# TODO: add mult, div, average....
# TODO: add time dimension
# TODO: add headers 
# TODO: column independence of the position, indexed by column header name 
# 
######

class Config:
    """ generic class to track the user parameters. main internal variable is a dictionary of lists.  """

    def __init__(self):
        """ generic class to track the user parameters. All variables shall be list or dictioneries """
        
        self.config = {}
        self.config[OPT_METRIC] = []
        self.config[OPT_DIM]    = []
        self.config[OPT_FILES]  = []

    def parse(self, args):
        """ fills the internal config dictionary by using the cli parameters as keys. """
        (options,files) = getopt.getopt(args, "h", [OPT_METRIC, OPT_DIM, OPT_FILES, OPT_HELP])

        for (o,v) in options:
            if o == "--metric":
               self.config[OPT_METRIC].append(int(v))
            elif o == "--dim":
               self.config[OPT_DIM].append(int(v))  # TODO ontology... need to add, shall be float..
            elif o == "-h":
               print usage()
               sys.exit(1)
            else:
               print "error [%s][%s]"% (args, o, v)
               print usage()
               sys.exit(1)

        self.config[OPT_FILES] = files

    def getFiles(self):
        """ return a list of configured files to be read. """
        return self.config[OPT_FILES]

    def getMetrics(self):
        """ return a list of configured metrics to be used. . """
        return self.config[OPT_METRIC]

    def getDims(self):
        return self.config[OPT_DIM]

    def usage(self):
        return """
Usage: collapser [--dim N].. [--metric]... files
   
       more than one dimension can be selected.
       more than one metric can be selected.
       more than one file can be selected.


       output in stdout.
"""

_config = None

def getConfig(args):
    """ configuration singleton. Config shall be instantiated calling this getConfig"""
    global _config

    if _config == None:
        _config = Config()
        _config.parse(args)

    return _config


    def __str__(self):
        s  = str(self.config[OPT_DIM])
        s += str(self.config[OPT_METRIC])
        return s
    

def collapserCallback(line, collapser):
    # TODO global variable... BAD....
    collapser.do(line)

def readFiles(files, dims, metrics):
    results = Collapser()
    results.init(dims, metrics)

    parseCSV(files, collapserCallback, results)

    return results

if __name__ == "__main__":
    config = getConfig(sys.argv[1:])
    result = readFiles(config.getFiles(), config.getDims(), config.getMetrics())
    print result 
