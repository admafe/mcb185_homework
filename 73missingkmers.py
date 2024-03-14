import gzip
import json
import sys
import mcb185

fasta = sys.agv[1]

for k in range(4,10):
	print('checking', k)
	#get all kmers for all sequences
	kcount = {}
	for defline, seq in mcb.read_fasta(fasta):
		for i in range(len(seq) -k +1):
			kmer = seq[i: i+k]
#			print(kmer)
			if kmer not in kcount: kcount[kmer] = 0
			kcount[kmer] += 1
			
	#check all kmers against all possible kmers
	if len(kcount.keys()) ==4**k: continue
#	print('missing at', k)

	#report missing kmers
	for ktup in itertools.product('ACGT', repeat =k):
		kmer = ''.join(ktup)
		if kmer not in kcount: print(kmer)
		
	sys.exit()
		