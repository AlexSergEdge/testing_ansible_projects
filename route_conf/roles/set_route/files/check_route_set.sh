#!/bin/sh
set -eu
set -o pipefail

# TODO - template this variables

IP_TABLE="$(route -n)"
ROUTE="192.168.2.0     192.168.122.1   255.255.255.0   UG    0      0        0 virbr0"
if echo "$IP_TABLE" | grep -q ""; then
    echo "Route found";
else
    echo "Route not found";
fi