#! /usr/bin/env python

# To use Python3 style in Python2
from __future__ import print_function
import sys
import os

input_file = sys.argv[1]
if (os.path.isfile(input_file)):
    print('File exists')
else:
    print('File does not exist', file=sys.stderr)