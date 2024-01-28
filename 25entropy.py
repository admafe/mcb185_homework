# 25entropy.py by Adele Ferrer
# Co-authors: David 

# Take in counts, find freq of each, then do summation
# Needs to account for and ignore 0 inputs (What if there is no T?)

#each nucleotide has
import math
import sys

def entropy(A, C, G, T):
	total = A + C + G + T
	pA = A / total
	pC = C / total
	pG = G / total 
	pT = T / total
	if   A <= 0: H = -(pC * math.log2(pC) + pG * math.log2(pG) + pT * math.log2(pT))
	elif C <= 0: H = -(pA * math.log2(pA) + pG * math.log2(pG) + pT * math.log2(pT))
	elif G <= 0: H = -(pA * math.log2(pA) + pC * math.log2(pC) + pT * math.log2(pT))
	elif T <= 0: H = -(pA * math.log2(pA) + pC * math.log2(pC) + pG * math.log2(pG))
	else:
		H = -(pA * math.log2(pA) + pC * math.log2(pC) + 
		      pG * math.log2(pG) + pT * math.log2(pT))
	return H

print(entropy(1, 1, 1, 1))
print(entropy(30, 14, 17, 12))
print(entropy(4, 0, 5, 7))
#print(entropy(5, 0, 6, 0))

#Note to self: cannot handle more than 1 zero input
#Figure out how to format to ignore parts of fxn when input is 0
