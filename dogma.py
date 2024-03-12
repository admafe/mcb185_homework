# dogma.py by Adele Ferrer

def transcribe(dna):
	return dna.replace('T','U')
	
def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if   nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')		
		else:           rc.append('N')
	return ''.join(rc)
	
def translate(dna):
	aas = []	
	for i in range(0, len(dna), 3):
		codon = dna[i: i + 3]
		if   codon == 'ATG': aas.append('M')
		elif codon == 'TAA': aas.append('*')
		else:                aas.append('X')
	return ''.join(aas)
	
def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)
	
def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return(g - c) / (g + c)
	
import math

def entropy(a, c, g, t):
	total = a + c + g + t
	assert(total != 0)
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
	
def hydrophobicity(aa):
	if   aa == 'A': return +1.8
	elif aa == 'C': return +2.5
	elif aa == 'D': return -3.5
	elif aa == 'E': return -3.5
	elif aa == 'F': return +2.8
	elif aa == 'G': return -0.4
	elif aa == 'H': return -3.2
	elif aa == 'I': return +4.5
	elif aa == 'K': return -3.9
	elif aa == 'L': return +3.8
	elif aa == 'M': return +1.9
	elif aa == 'N': return -3.5
	elif aa == 'P': return -1.6
	elif aa == 'Q': return -3.5
	elif aa == 'R': return -4.5
	elif aa == 'S': return -0.8
	elif aa == 'T': return -0.7
	elif aa == 'V': return +4.2
	elif aa == 'W': return -0.9
	elif aa == 'Y': return -1.3
	else:           return 0.0
