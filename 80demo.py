# 80demo.py by Adele Ferrer

import json
import mcb185
import sys

import gzip	

'''
k = int(sys.argv[2])
kcount= {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq)-k +1):
	kmer = seq[i: i+k]
	if kmer not in kcount:kcount[kmer] = 0
#	if kmer not in kcount: kcount[kmer] = 1
#	else:                  kcount[kmer] += 1
print(json.dumps(kcount, indent=4))
'''
'''
k = int(sys.argv[2])
kloc= {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	words = defline.split()
	chrom = words[0]
	for i in range(len(seq)-k +1):
		kmer = seq[i: i+k]
		if kmer not in kloc: kloc[kmer] = {}
		if chrom not in kloc[kmer]: kloc[kmer][chrom] = []
		kloc[kmer][chrom].append(i)
#	kloc[kmer].append( (chrom, i))
	
print(json.dumps(kloc, indent=4))
'''
'''
person = {
	'name': 'Ian Korf',
	'age': 57,
	'weight': 163.8,
	'marries': True,
	'pets': ['Hesper', 'Mouserat', 'Labrat'],
	'mentees': {
		'Claire': 'undergrad',
		'Dell': 'undergrad',
	}
}

people = []
people.append(person)

people[0]['gibberish'] = 'hello'
#people[0]['mentees']['Ismael']

print(json.dumps(people, indent=4))

#print(people[0]['mentees']['Claire'])
'''

'''
import sys

print(sys.argv[1])

print(sys.argv[1][2])

matrix = [
	[1, 2, 3],
	[4, 5, 6, 7, [8, 9]], #nested hierarchy 
]

print(matrix)
print(matrix[1][0])
'''

introns = []
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		f = line.split()
		if f[2] != 'intron': continue
		chrom = f[0]
		beg =int(f[3]) - 1
		end = int(f[4]) -1
		strand = f[6]
		score = int(f[5])
#		introns.append( (chrom, beg, end, strand, n) )
		if chrom not in introns: introns[chrom] = []
		introns.append({
			'chrom': chrom, 
			'beg': beg,
			'end': end, 
			'strand': strand,
			'count': n })
			
dons = []
accs = []
dlen =6
aclen = 8
for i in range(dlen):
	dons.append( {'A':0, 'C':0, 'G':0, 'T':0} )
for i in range(aclen):
	accs.append( {'A':0, 'C':0, 'G':0, 'T':0} )		
			
for defline, seq in mcb185.read_fasta(sys.argv[2]):
	words = defline.split()
	chrom = words[0]
	for c, b, e, s, n in introns:
		if chrom == c:
			iseq = seq[b:e+1]
			if s =='-': iseq = mcb.anti_seq(iseq)
			don = iseq[:6]
			acc = isesq[-8:]
			print(don, acc)
	
print(json.dumps(introns, indent =4))