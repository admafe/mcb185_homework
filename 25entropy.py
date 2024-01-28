# 25entropy.py by Adele Ferrer
# David 

#frequencies of diff nucleotides in 
# -sum of probabilities of each of the nucleotide frequencies multiplied but log of each prob

#take in counts or frequencies, find freq of each; then do summation; 
#needs to ignore the 0 inputs (what if there is no t or something)

#each nucleotide has
import math

def entropy(A, C, G, T):
	total = A + C + G + T
	pA = A / total
	pC = C / total
	pG = G / total 
	pT = T / total
	return -((pA * math.log2(pA)) + (pC * math.log2(pC)) +
			 (pG * math.log2(pG)) + (pT * math.log2(pT)))

print(entropy(1,1,1,1))
print(entropy(4,0,5,7))
