#!/usr/bin/env python

import sys


for l in sys.stdin:
    in_list = l.split()
    pr = float(in_list[-1])
    num_links = len(in_list) - 2  # -2 for the source page and the pr
    to_pages = in_list[1:-1]
    from_page = in_list[0]
    to_pages_str = ''
    for p in to_pages:
        to_pages_str += p + ' '
        print('%s\t%s,%s' % (p, from_page, pr / num_links))
    print('%s\t%s' % (from_page, to_pages_str[:-1]))
