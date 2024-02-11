# 44randompi.py by Adele Ferrer
# Co-author: Marle Lamountry

import random
import math

inside = 0
outside = 0
while True:
	x = random.random()
	y = random.random()
	distance = math.sqrt(x**2 + y**2)
	if distance < 1: inside += 1
	else:            outside += 1
	pi = 4 * (inside / (inside + outside))
	print(pi)
