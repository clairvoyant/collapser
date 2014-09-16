#!/usr/bin/env python

"""  is a class that takes a csv file as input and perform aritmetic operations in the
    columns. 

    The output will be the diferent rows colapsed into the key fields. 
"""
def safeint(s):
    result = 0

    try:
       result = int(s)
    except:
       pass

    return result


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
         
        dimkey = ','.join([record[dim] for dim in self.dimsColumns ])

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
        result = ""         
        for row in iter(self):
            result += ','.join([str(field) for field in row])
            result += '\n'
        return result
        
     def __iter__(self):
         """generator it returns a row with 
            concatenated keys. Note the dimensions are inside the same string
                ["key1,key2", A,B,C]
         """
         
         dimKeys = self.results.keys()
         dimKeys.sort() 
         for dimKey in dimKeys:
             dimRow = self.results[dimKey]
             result = [dimKey]
             for metricCol in dimRow.keys():
                 metricVal = dimRow[metricCol]
                 result.append(metricVal)
             yield result
         return

