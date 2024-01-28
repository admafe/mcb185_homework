# 25entropy.py by Adele Ferrer 

# Take in counts, find freq of each, then do summation
# Needs to account for and ignore 0 inputs (What if there is no T?)

#		H = -(pA * math.log2(pA) + pC * math.log2(pC) + 
#		      pG * math.log2(pG) + pT * math.log2(pT))

import math
import sys

def entropy(A, C, G, T):
	total = A + C + G + T
	pA = A / total
	pC = C / total
	pG = G / total 
	pT = T / total
	H = 0
	if A > 0: H = H + pA * math.log2(pA)
	if C > 0: H = H + pC * math.log2(pC)
	if G > 0: H = H + pG * math.log2(pG)
	if T > 0: H = H + pT * math.log2(pT)
	return -H

print(entropy(1, 1, 1, 1))
print(entropy(30, 14, 17, 12))
print(entropy(4, 0, 5, 7))
print(entropy(5, 0, 6, 0))
