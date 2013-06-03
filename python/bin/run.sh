#!/bin/bash

base=`dirname $0`

export PYTHONPATH=$PYTHONPATH:${base}/../lib

exec ${base}/collapser.py --dim=0 --metric=1 ${base}/../../test/01.csv


