# 45dndstats.py by Adele Ferrer

import random

rolls = 10000

# 3D6
total = 0
for i in range (rolls):
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	score = d1 + d2 + d3
	total += score
#print(score)
print(total / rolls)

# 3D6r1
total = 0
for i in range (rolls):
	d1 = random.randint(1, 6)
	if d1 == 1: d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	if d2 == 1: d2 == random.randint(1, 6)
	d3 = random.randint(1, 6)
	if d3 == 1: d3 == random.randint(1, 6)
	score = d1 + d2 + d3
	total += score
#print(d1, d2, d3)
#print(score)
print(total / rolls)

# 3D6x2
total = 0
for i in range (rolls):
	score = 0 
	for j in range(3):
		d1 = random.randint(1,6)
		d2 = random.randint(1,6)
		if d1 < d2: keep = d2
		else:       keep = d1
		score += keep
#		print('d1', d1, 'd2', d2)
#		print(keep)
	total += score
#	print(score)
print(total / rolls)


# 4D6d1
total = 0 
for i in range(rolls):
	score = 0
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	d4 = random.randint(1, 6)
	if   d1 < d2 and d1 < d3 and d1 < d4: score = d2 + d3 + d4
	elif d2 < d1 and d2 < d3 and d2 < d4: score = d1 + d3 + d4
	elif d3 < d1 and d3 < d2 and d3 < d4: score = d1 + d2 + d4
	else: score = d1 + d2 +d3
	total += score
#	print(d1, d2, d3, d4)
#	print(score)
print(total / rolls)
