# 25entropy.py by Adele Ferrer 

# Take in counts, find freq of each, then do summation
# Needs to account for and ignore 0 counts
# (What if there is no T?)

#		H = -(PA * math.log2(PA) + PC * math.log2(PC) + 
#		      PG * math.log2(PG) + PT * math.log2(PT))

import math
import sys

def entropy(A, C, G, T):
	total = A + C + G + T
	PA = A / total
	PC = C / total
	PG = G / total 
	PT = T / total
	H = 0
	if A > 0: H = H + PA * math.log2(PA)
	if C > 0: H = H + PC * math.log2(PC)
	if G > 0: H = H + PG * math.log2(PG)
	if T > 0: H = H + PT * math.log2(PT)
	return -H

print(entropy(1, 1, 1, 1))
print(entropy(30, 14, 17, 12))
print(entropy(4, 0, 5, 7))
print(entropy(5, 0, 6, 0))
