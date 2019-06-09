#!/usr/bin/env python

import re
import sys

match_list = ['hackathon', 'Dec', 'Chicago', 'Java']

for l in sys.stdin:
    for word in match_list:
        if word.lower() in l.lower():
            print "%s\t%s" % (word, 1)
