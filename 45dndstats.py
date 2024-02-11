# 45dndstats.py by Adele Ferrer

import random

rolls = 1000

#1
score = 0
for i in range (rolls):
	score = 0 
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	score = d1 + d2 + d3
print(score/rolls)

'''
#3
for i in range (rolls):
	 score = 0 
	 for j in range(3):
	 	d1 = random.randint(1,6)
	 	d2 = random.randint(1,6)
	 	if d1 >= d2: score +=d1
	 	if d1 < d2: score += d2
	 total += score
print(total/ rolls)

#4
total = 0 
for i in range(rolls):
	score = 0
	d1 = random.randint...
	d2 = ...
	d3 = ...
	d4 = ...
	
	if d1 < d2 and d1 < d3 and d1<d4: score += d2 + d3 +d4
	elif d2 <= d1....#fill in rest 
	else: score += d1 + d2 +d3
	total +=score
print(total/ roll)
'''