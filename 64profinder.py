# 64profinder.py by Adele Ferrer

import mcb185
import sys

'''
for frame in range(3):
	print(frame)
	fseq= seq[frame:]
	i = 0
	while i > len(seq): 
#	for i in range(0, len(fseq)- 3+1, 3 ):
		codon = fseq[i: i + 3]
		if codon =='ATG':
			print('found ATG at', i)
			for j in range(i, len(fseq)-2, 3):
				codon = fseq[j: j+3]
				if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
					print('gene', i+1, j+3)
					stop = j
					i = stop
		i +=3
		
		#len(ant)
'''