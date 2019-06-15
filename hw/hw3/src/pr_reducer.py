#!/usr/bin/env python

import sys

last_k = None

cur_page_map = None
cur_pr_sum = 0.

for l in sys.stdin:
    # processing the keys
    (k, v) = l.strip().split("\t")
    split_v = v.split(",")

    if last_k and last_k != k:
        # when the key changes
        print("%s %s %s" % (last_k, cur_page_map, cur_pr_sum))

        # resetting
        cur_page_map = None
        cur_pr_sum = 0.

    # updating the state
    if len(split_v) > 1:
        # is a pr row
        cur_pr_sum += float(split_v[-1])
    else:
        # is a map row
        cur_page_map = split_v[0]

    last_k = k

# last key
if last_k:
    print("%s %s %s" % (last_k, cur_page_map, cur_pr_sum))

