#Make a random protein

#Dictionaries are faster!!! than lists 
#Dictionaries used for fast lookups  
#

import random
#random.seed(1)

size = 10000
#words = {}
wordd = {}
for i in range(size):
	token = []
	for j in range(10):
		token.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	token = ''.join(token)
#	words.append(token)
#	words[token] = True
	wordd[token] = True
print(words)
	
for i in range(1000):	
	if 'MYNAMEISIAN' in words:
#		idx = words.index(word)
		print('found')

"""
#Can also do global values, capitalize those
#not as fast, not as good, don't use very often 
'''
AAS = 'IVLFCMAGTSWYPHEQDNKR'
KDS = (4.5, 4.3, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4,
		-0.7, -0.8, -0.9, -1.3, -1.6, -3.2, -3.5, 
		-3.5, -3.5, -3.5, -3.9, -4.5, 0 )
'''
#prettier looking, not as fast 
def kdh_stack(seq):
	kds = 0
	for aa in seq:
		if   aa == 'A': return +1.8
		elif aa == 'C': return +2.5
		elif aa == 'D': return -3.5
		elif aa == 'E': return -3.5
		elif aa == 'F': return +2.8
		elif aa == 'G': return -0.4
		elif aa == 'H': return -3.2
		elif aa == 'I': return +4.5
		elif aa == 'K': return -3.9
		elif aa == 'L': return +3.8
		elif aa == 'M': return +1.9
		elif aa == 'N': return -3.5
		elif aa == 'P': return -1.6
		elif aa == 'Q': return -3.5
		elif aa == 'R': return -4.5
		elif aa == 'S': return -0.8
		elif aa == 'T': return -0.7
		elif aa == 'V': return +4.2
		elif aa == 'W': return -0.9
		elif aa == 'Y': return -1.3
		else:           return 0.0
	return kds/len(seq)
	
#not as clear but faster than list 
def kdh_list(seq):
	kdsum = 0
	aas = 'IVLFCMAGTSWYPHEQDNKR'
	kds = (4.5, 4.3, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4,
		-0.7, -0.8, -0.9, -1.3, -1.6, -3.2, -3.5, 
		-3.5, -3.5, -3.5, -3.9, -4.5, 0 )
	for aa in seq:
		idx = aas.index(aa)
		kdsum = kds[idx]
	return kdsum/ len(seq)
	
KDT = {
    'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kdh_dict(seq):
	kdsum = 0 
	for aa in seq:
		if aa in KDT: kdsum += KDT[aa]
	return kdsum / len(seq)

protein_length = 100
protein = []
for i in range(protein_length):
	aa = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	protein.append(aa)	
protein= ''.join(protein)
print(protein)

for i in range(1000):
	kdh_stack(protein)
	kdh_list(protein)
"""
