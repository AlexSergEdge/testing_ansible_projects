#! /usr/bin/env python
import sys
import json

# Get data from command line
json_data = sys.argv[1]
assert '192.168.2.0     192.168.122.1   255.255.255.0   UG    0      0        0 virbr0' in json_data