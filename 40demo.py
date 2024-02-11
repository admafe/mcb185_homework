# 40demo.py by Adele Ferrer

import random

'''
for i in range(5):
	print(random.random())


for i in range(50):
	r = random.random()
	if r < 0.7: print(random.choice('AT'), end = '')
	else:       print(random.choice('CG'), end = '')
print()

for i in range(3):
	print(random.randint(1, 6))

for i in range(5):
	print(random.gauss(0.0, 1.0))
'''
'''
nts = 'ACGT'

for nt in nts:
	print(nt, end=' ')
	
print()

for i in range(3):
#	print('>seq-', i, sep = '')
	print(f'>seq-{i + 1}')
	for j in range(random.randint(20, 50)):
		print(random.choice(nts), end = '')
	print()
	
for nt1 in nts:
	for nt2 in nts:
		if nt1 > nt2:
			print('outer', nt1, 'inner', nt2)
			
limit = 10
for i in range(0, limit):
		for j in range(0, limit):
			if i == j: print('+', end = ' ') 
			else:      print('-', end = ' ')
		print()
#			print(i , j)
'''
# Pretty Printing
'''
print(10, 20, 30, 40, sep = '\t')
print(100, 2000, 30000, 40000, sep = '\t')

i = 1
pi = 3.14159
print('normal string {i} {pi}')
print(f'formatted string {i} {pi:.3f}')
print(f'tau {pi + pi}')
'''

import sys
print('logging', file=sys.stderr)

random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())