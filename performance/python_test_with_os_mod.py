#!/usr/bin/python

import os

LOOP = 0
bar = "test"
foo = ""

while LOOP < 1000000:
        if bar and not foo:
                os.system('echo "ok" >> /dev/null')
        LOOP=LOOP + 1
