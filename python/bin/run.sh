#!/bin/bash

base=`dirname $0`

exec ${base}/correlator.py --dim=0 --metric=1 ${base}/../test/three.csv


