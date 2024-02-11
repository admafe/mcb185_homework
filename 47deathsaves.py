# 47deathsaves.py by Adele Ferrer

import random

rolls = 100000

deaths = 0
stable = 0
revives = 0
for i in range(rolls):
	failures = 0
	successes = 0
	for j in range(3):
		d1 = random.randint(1, 20)
		if 1 < d1 < 10:   failures += 1
		if 20 > d1 >= 10: successes += 1
		if d1 == 1:       failures += 2
		if d1 == 20:      revives += 1
#		print(d1)
#	print(f'Failures: {failures}', f'Successes: {successes}')
	if failures >= 3: deaths += 1
	if successes == 3: stable += 1

print(deaths/rolls, stable/rolls, revives/rolls)