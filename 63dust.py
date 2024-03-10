# 63dust.py by Adele Ferrer
# Co-author: Natalia Marin

#head ecoli.fa.gz > mini
#extracts a small test section of ecoli genome 
#it's in unit 1 

#find areas where the entropy falls below threshold of 1.4, in any given window

#Command line: python3 63dust.py ecoli.fa.gz 20 1.4

import sys
import math
import mcb185
import dogma

#window first
#count later

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	sequence = list(seq)	
w = int(sys.argv[2])
h = float(sys.argv[3])

for i in range(len(sequence) - w +1):
	window = sequence[i : i+w]
	for n in window: 
		a = sequence[0:w].count('A')
		c = sequence[0:w].count('C')
		g = sequence[0:w].count('G')
		t = sequence[0:w].count('T')
		if dogma.entropy(a, c, g, t) < h:
			for n in window:
				window[n] = 'N'

masked_seq = ''.join(window)
print(masked_seq)


