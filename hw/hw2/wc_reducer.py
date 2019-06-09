import sys

last_k = None
cur_c = 0

for l in sys.stdin:
    (k, v) = l.strip().split("\t")
    if last_k and last_k != k:
        print "%s\t%s" % (last_k, cur_c)
        cur_c = 1
        last_k = k
    else:
        last_k = k
        cur_c += 1

if last_k:
    print "%s\t%s" % (last_k, cur_c)
