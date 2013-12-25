#!/bin/sh


dir=$(dirname $0)

py.test --junitxml $dir/results.xml $dir/test.py
