#!/usr/bin/env python

import sys

# initializations
last_k = None
base_dict = {
    'min': None,
    'max': None,
    'sum': 0.,
    'cnt': 0,
    'cnt_null': 0
}  # should never change
attrib_order = ['temp', 'humid', 'pres', 'winddir', 'windspeed', 'skycond', 'precip1', 'precip6']
cur_sum_dict = {}
for attrib_name in attrib_order:
    cur_sum_dict[attrib_name] = base_dict.copy()


# some helper functions
def agg_handle_null(v1, v2, agg_fn):
    """ handles the updates during the loop to the internal dict"""
    if v1 is None:
        return v2
    elif v2 is None:
        return v1
    else:
        return agg_fn(v1, v2)


def do_print(key, cur_dict):
    """ prints the finished data summary"""
    to_print = str(key)
    for a_name in attrib_order:
        to_print += "," + str(cur_dict[a_name]['max'])
        to_print += "," + str(cur_dict[a_name]['min'])
        to_print += "," + str(cur_dict[a_name]['sum'])
        to_print += "," + str(cur_dict[a_name]['cnt'])
        to_print += "," + str(cur_dict[a_name]['cnt_null'])
    print(to_print)


for l in sys.stdin:
    # reading the lines in
    k, vs = l.strip().split("\t")
    vl = vs.split(",")

    # parsing and casting the input
    cur_attribs = {
        'temp': float(vl[0]),
        'humid': float(vl[1]),
        'pres': float(vl[2]),
        'winddir': int(vl[3]),
        'windspeed': float(vl[4]),
        'skycond': int(vl[5]),
        'precip1': float(vl[6]),
        'precip6': float(vl[7]),
    }

    if last_k and last_k != k:
        do_print(last_k, cur_sum_dict)

        # resetting
        cur_sum_dict = {}
        for attrib_name in attrib_order:
            cur_sum_dict[attrib_name] = base_dict.copy()

    # handling a new value
    for attrib_name in attrib_order:
        cur_v = cur_attribs[attrib_name]
        cur_to_dict = cur_sum_dict[attrib_name]

        if cur_v != -9999:
            cur_to_dict['min'] = agg_handle_null(cur_to_dict['min'], cur_v, min)
            cur_to_dict['max'] = agg_handle_null(cur_to_dict['max'], cur_v, max)
            cur_to_dict['sum'] += cur_v
            cur_to_dict['cnt'] += 1
        else:
            cur_to_dict['cnt_null'] += 1

    last_k = k

if last_k:
    do_print(last_k, cur_sum_dict)
