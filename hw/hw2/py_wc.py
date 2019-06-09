import sys


match_list = ['hackathon', 'Dec', 'Chicago', 'Java']
matched_dict = dict(zip(match_list, [0]*4))
for l in sys.stdin:
    for word in match_list:
        if word.lower() in l.lower():
            matched_dict[word] += 1

for k in matched_dict:
    print(k, matched_dict[k])
