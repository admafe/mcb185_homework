# 65transmembrane.py by Adele Ferrer
# Co-Author: Marle Lamountry 

import mcb185
import sys
import dogma

signallength

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	protein = list(seq)
	for i in range(len(protein)):
		for j in range(protein[:30], )
'''
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	#first 30 is signal?
	#after first 30 is transmembrane?

for i in range(len(protein)):
	for j in range(protein[:30], -signallength +1):
	window = prot[j: j - signallength]
	avgKDH = #calculate hydrophobcity for each 
'''
'''
search first 30 for signal
search after that for transmembrane bit
'''
