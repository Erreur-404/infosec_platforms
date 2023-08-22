#!/bin/bash
cd /home/$(whoami)/Downloads/temp
echo $(echo "00000000: $1" | xxd -r - query.decoded.small | base64 query.decoded.small | tr -d '\n')