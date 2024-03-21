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

w = int(sys.argv[2])
h = float(sys.argv[3])
masked_seq = []	

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	sequence = list(seq)	
	for i in range(len(seq) - w +1):
		window = seq[i : i+w]
		a = window.count('A')
		c = window.count('C')
		g = window.count('G')
		t = window.count('T')
		if dogma.entropy(a, c, g, t) < h:
			for j in range(i, i+w):
				sequence[j] = 'N'
	print(defline, ''.join(sequence))


