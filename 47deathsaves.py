# 47deathsaves.py by Adele Ferrer

import random

rolls = 10000

deaths = 0
stable = 0
revives = 0
for i in range(rolls):
	failures = 0
	successes = 0
	while True:
		d1 = random.randint(1, 20)
		if d1 == 20:
			revives += 1 
			break
		elif d1 >= 10:
			successes += 1
		elif d1 == 1:
			failures += 2
		else:
			failures += 1
		if failures >= 3:
			deaths += 1
			break
		elif successes >= 3:
			stable += 1
			break
#		print(d1)
#	print(f'Failures: {failures}', f'Successes: {successes}')

print(deaths/rolls, stable/rolls, revives/rolls)