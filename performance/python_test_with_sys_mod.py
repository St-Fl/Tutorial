#!/usr/bin/python

import os
import sys

LOOP = 0
bar = "test"
foo = ""

sys.stdout = open(os.devnull, 'w')

while LOOP < 1000000:
        if bar and not foo:
                print LOOP
                #os.system('echo "ok" >> /dev/null')
        LOOP=LOOP + 1
