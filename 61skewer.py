# 61skewer.py by Adele Ferrer

import dogma
import sys
import mcb185

'''
calculating G-C composition in window of sequence
count G-C pairs, count how many in window
needing to slide the window (reading frame) over

61: move over window, then recalculate, slide, recount
62: just calculate once, add next letter, take off first letter
'''
#Command Line: python3 61skewer.py ecoli.fa.gz 1000 

w = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) - w + 1):
		s = seq[i: i+w]
		dogma.gc_comp(s)
		dogma.gc_skew(s)
		print(f'{i}\t{dogma.gc_comp(s):.3f}\t{dogma.gc_skew(s):.3f}')

		