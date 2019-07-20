#!/usr/bin/env python

import sys

for l in sys.stdin:
    a = l.split()

    year = a[0]
    month = a[1]
    day = a[2]
    hour = a[3]
    temp = a[4]
    humid = a[5]
    pres = a[6]
    winddir = a[7]
    windspeed = a[8]
    skycond = a[9]
    precip1 = a[10]
    precip6 = a[11]
    station_id = a[12]

    print('%s-%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (year,
                                                       month,
                                                       day,
                                                       hour,
                                                       temp,
                                                       humid,
                                                       pres,
                                                       winddir,
                                                       windspeed,
                                                       skycond,
                                                       precip1,
                                                       precip6,
                                                       station_id))
