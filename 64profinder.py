# 64profinder.py by Adele Ferrer
# Co-Author: Yutong Ji

import mcb185
import sys
import dogma

min_length = int(sys.argv[2])

def sixframe_trans(seq):
		translations = []
		for frame in range(3):
			aa_seq = dogma.translate(seq[frame:]).split('*')
			for aa in aa_seq:
				if 'M' in aa:
					protein = aa[aa.find('M'):]
					if len(protein) >= min_length:
						translations.append(protein)
		return translations

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	forward = sixframe_trans(seq)
	reverse = sixframe_trans(dogma.revcomp(seq))
	for protein in reverse:
		forward.append(protein)
	for i, protein in enumerate(forward):
		print(f'>{defline[:11]}-prot-{i}\n{protein}*')
		

	
	
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