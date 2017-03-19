#!/bin/bash

# vars
LOOP=0
bar="test"
foo=""

# while count to messure reasonable the performance
while [ $LOOP -lt 1000000 ] ; do
	# if [] && [] VS test -a - performance measurement 
	if test -n "bar" -a "foo" != "null"; then  echo "ok" >> /dev/null ; fi	
  LOOP=$((LOOP + 1))
done
