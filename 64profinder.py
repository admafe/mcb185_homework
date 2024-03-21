# 64profinder.py by Adele Ferrer
# Co-Author: Yutong Ji

import mcb185
import sys
import dogma

min_length = sys.argv[2]

def sixframe_trans(seq):
		translations = []
		anti_seq = dogma.revcomp(seq)
		for frame in range(3):
			forward_trans = dogma.translate(seq[frame:]).split('*')
			reverse_trans = dogma.translate(anti_seq[frame:]).split('*')
			for aa in translations:
				if 'M' in aa:
				protein = aa[aa.find('M'):]
				if len(prot) >= min_length:
					translations.append(forward_trans)
					translations.append(reverse_trans)
		return translations

for defline, seq in mcb185.read_fasta(sys.argv[1]):
		for aa in translations:
			if aa == 'M': break
	print(translations)
	
#	aa_seq = dogma.translate(seq)
#	for i in range(0, len(aa_seq) - frame + 1, 1):
#		if i == 'M': print('found start codon', i)


'''
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for frame in range(3):
		print(frame)
		stop_used = {}
		fseq= seq[frame:]
#		i = 0
#		while i > len(seq): 
		for i in range(0, len(fseq) - 3 + 1, 3):
			codon = fseq[i: i+3]
			if codon != 'ATG':
#				print('found ATG at', i)
				for j in range(i, len(fseq)-2, 3):
					codon = fseq[j: j+3]
					if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
						stop = j
						if stop not in stop_used: 
							print('gene', i+1, j+3)
							stop_used[stop] = True
#						i = stop
		i +=3
		
		#len(ant)
'''