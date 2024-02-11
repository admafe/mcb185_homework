# 43randomdna.py by Adele Ferrer

import random

nts = 'ACGT'
for i in range(3):
#	print('>seq-', i, sep = '')
	print(f'>seq-{i + 1}')
	for j in range(random.randint(25, 50)):
		print(random.choice(nts), end = '')
	print()