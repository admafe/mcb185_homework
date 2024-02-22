# 60demo.py by Adele Ferrer

import mcb185 

#alias in command line
ln - s ../MCB185?src/mcb185.py
	
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	pro = []
	print(defline, seq[:30])
	for i in range(0, len(seq), 3):
		codon = seq[i: i +3]
		aa = translate
