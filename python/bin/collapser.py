#!/usr/bin/env python

"""  is a class that takes a csv file as input and perform aritmetic operations in the
    columns. 

    The output will be the diferent rows colapsed into the key fields. 
"""

import sys
import getopt
import csv

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

def safeint(s):
    result = 0

    try:
       result = int(s)
    except:
       pass

    return result

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
    

class Collapser:

     """ configuration singleton. Config shall be instantiated calling this getConfig"""
     def init(self, dims, metrics):
        self.dimsColumns    = dims
        self.metricsColumns = metrics
        self.results        = {}

                
     def do(self, record):
        """ algoritm is straighforward. use the dims as a dictionary to index diferent values. 
             Add the counters/metrics per key. 
             if more than one key is configured, then agregate them in order to make a unique key.
             
             record: shall be a list of values. if the len is not enought, then return."""
         
        dimkey = ""
        for dim in self.dimsColumns:
            if len(record) < dim:
               return # not enough info
            dimkey += record[dim] + ','

        if not dimkey in self.results:
           self.results[dimkey] =  {}

        row = self.results[dimkey]

        for metric in self.metricsColumns:
            if len(record) < metric:
               return # not enough info

            # perform adition
            if not metric in row:
               row[metric] = 0
            row[metric] += safeint(record[metric])

     def __str__(self):
        """ return a comma separated representation of each element in the record """
        result = ''
        for dimKey in self.results.keys():
            dimRow = self.results[dimKey]
            s      = ''

            first=True

            for metricCol in dimRow.keys():
                metricVal = dimRow[metricCol]
                if first:
                   first = False
                   s += str(metricVal)
                else:
                   s += ','+ str(metricVal)

            result += dimKey + s +"\n"


        return result


def collapserCallback(line, collapser):
    # TODO global variable... BAD....
    collapser.do(line)

def parseCSV(file, cb, param):
    """ implement a csv reader reactor, the callback is executed per each csv record. """
    
    # TODO read gz and bz compresed csv files.
    
    f = open(file, "r")
    reader = csv.reader(f)

    for row in reader:
        cb(row, param)

    f.close()

def readFiles(files, dims, metrics):
    results = Collapser()
    results.init(dims, metrics)

    for file in files:
        parseCSV(file, collapserCallback, results)

    return results

if __name__ == "__main__":
    config = getConfig(sys.argv[1:])
    result = readFiles(config.getFiles(), config.getDims(), config.getMetrics())
    print result 
