#!/usr/bin/env python

import sys

# initializing
attrib_order = ['temp', 'humid', 'pres', 'winddir', 'windspeed', 'skycond', 'precip1', 'precip6']
field_order = ['max', 'min', 'sum', 'cnt', 'cnt_null']
base_dict = {
    'min': None,
    'max': None,
    'sum': 0.,
    'cnt': 0,
    'cnt_null': 0
}
last_k = None
res_dict = {}
for attrib_name in attrib_order:
    res_dict[attrib_name] = base_dict.copy()


# some helper functions
def do_print(cur_k, results_dict):
    cur_line = cur_k
    for ca in attrib_order:
        for cf in field_order:
            cur_line += "," + str(results_dict[ca][cf])
    print(cur_line)


def agg_handle_null(v1, v2, agg_fn):
    """ handles the updates during the loop to the internal dict"""
    if v1 is None:
        return v2
    elif v2 is None:
        return v1
    else:
        return agg_fn(v1, v2)


for l in sys.stdin:
    k, v = l.split("\t")
    a = v.split()

    # putting fields in memory
    cf_dict = {}
    i = 0
    for cur_attrib in attrib_order:
        cf_dict[cur_attrib] = {}
        for cur_field in field_order:
            cf_dict[cur_field] = a[i]
            i += 1

    if last_k and last_k != k:
        do_print(last_k, res_dict)

        # resetting
        res_dict = {}
        for attrib_name in attrib_order:
            res_dict[attrib_name] = base_dict.copy()

    # handling a new value
    for cur_attrib in attrib_order:
        for cur_field in field_order:
            cur_v = cf_dict[cur_attrib][cur_field]
            if cur_v == 'None':  # means all of the entries were null when rolled up
                pass
            else:
                cur_v = float(cur_v)
                if cur_field == 'max':
                    res_dict[cur_attrib][cur_field] = agg_handle_null(cur_v, res_dict[cur_attrib][cur_field], max)
                elif cur_field == 'min':
                    res_dict[cur_attrib][cur_field] = agg_handle_null(cur_v, res_dict[cur_attrib][cur_field], min)
                else:
                    res_dict[cur_attrib][cur_field] += cur_v

    last_k = k

# print last key
if last_k:
    do_print(last_k, res_dict)
