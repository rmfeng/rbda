#!/usr/bin/env python

import sys

for l in sys.stdin:
    print("%s\t%s" % ("1", l[l.find(",") + 1:]))







