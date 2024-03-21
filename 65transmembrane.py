# 65transmembrane.py by Adele Ferrer
# Co-Author: Marle Lamountry, Aman Panigrahi

import mcb185
import sys
import dogma

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	signal = False
	transmem = False
	if len(seq) > 30:
		for i in range(0 , 23):
			if (seq[i: i+8].find('P') == -1 
			and dogma.avg_hydrophobicity(seq[i: i+8]) >= 2.5): signal = True
	if signal is True:
		for i in range(30, len(seq) -10):
			if (seq[i: i+11].find('P') == -1 
			and dogma.avg_hydrophobicity(seq[i: i+8]) >= 2.5): transmem = True
	if transmem is True: print(f'>{defline}')	

'''
search first 30 for signal
search after that for transmembrane bit

window = prot[j: j - 8]
avgKDH = #calculate hydrophobcity for each 
'''
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
