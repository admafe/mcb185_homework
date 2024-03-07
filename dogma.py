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
	
