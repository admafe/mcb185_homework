# 65transmembrane.py by Adele Ferrer
# Co-Author: Marle Lamountry 

import mcb185
import sys
import dogma
'''
def is_transmembrane(seq):
	signal_reg = seq[:30]
	transmem_reg = seq[30:]
	for i in range(len(signal_reg) - 7):
		signal = signal_reg[i: i+8]
		avg_kdh = 0
		for n in signal:
			dogma.hydrophobicity(signal)
'''
'''
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	protein = list(seq)
	for i in range(len(protein)):
		for j in range(protein[:30], )
'''

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	signal = seq[:30]
	transmem = seq[30:]
	for i in range(len(seq)):
		for j in range(seq[:30] -8 +1):
		window = prot[j: j - signallength]
		avgKDH = #calculate hydrophobcity for each 

'''
search first 30 for signal
search after that for transmembrane bit
'''
