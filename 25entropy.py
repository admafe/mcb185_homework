# 25entropy.py by Adele Ferrer 

# Take in counts, find freq of each, then do summation
# Needs to account for and ignore 0 counts
# (What if there is no T?)

#		H = -(PA * math.log2(PA) + PC * math.log2(PC) + 
#		      PG * math.log2(PG) + PT * math.log2(PT))

import math
import sys

def entropy(a, c, g, t):
	total = a + c + g + t
#	assert(total != 0)
	pa = a / total
	pc = c / total
	pg = g / total 
	pt = t / total
	h = 0
	if a > 0: h = h + pa * math.log2(pa)
	if c > 0: h = h + pc * math.log2(pc)
	if g > 0: h = h + pg * math.log2(pg)
	if t > 0: h = h + pt * math.log2(pt)
	return -h

print(entropy(1, 1, 1, 1))
print(entropy(30, 14, 17, 12))
print(entropy(4, 0, 5, 7))
print(entropy(5, 0, 6, 0))

# functions and variable need lowercase 