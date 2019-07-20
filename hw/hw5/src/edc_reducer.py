#!/usr/bin/env python

import sys

last_k = None

cur_max = None
cur_min = None
cur_sum = 0.
cur_cnt = 0

for l in sys.stdin:
    k, v = l.strip().split("\t")
    v = float(v)

    if last_k and last_k != k:
        print("%s, %s, %s, %s" % (k, cur_max, cur_min, cur_sum / cur_cnt))

        # resetting
        cur_max = None
        cur_min = None
        cur_sum = 0.
        cur_cnt = 0

    # if we have a null row, ignore it
    if v != -9999:
        cur_cnt += 1
        if cur_max is None:
            cur_max = v
        else:
            cur_max = max(v, cur_max)

        if cur_min is None:
            cur_min = v
        else:
            cur_min = min(v, cur_min)
        cur_sum += v

    last_k = k

if last_k:
    print("%s, %s, %s, %s" % (k, cur_max, cur_min, cur_sum / cur_cnt))