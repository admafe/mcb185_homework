# 51cdslength.py by Adele Ferrer

import gzip
import sys

lengths = []

#path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'
path = sys.argv[1]
with gzip.open(path, 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue
		words = line.split()
		if words[2] != 'CDS': continue
		beg = int(words[3])		
		end = int(words[4])
		lengths.append(end - beg + 1)
		
print(lengths)