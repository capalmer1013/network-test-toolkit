#!/usr/bin/python
# https://blog.petrzemek.net/2014/03/23/restarting-a-python-script-within-itself/
import sys
import os

print "starting..."
os.execv(__file__, sys.argv)
print "restarting the second way"
os.execv(sys.executable, ['python'] + sys.argv)
