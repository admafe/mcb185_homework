# 21quadratic.py by Adele Ferrer

import math

def quadratic(a, b, c):
	dis = b**2 - 4*a*c
	if(b**2 - 4*a*c) < 0: 
		return "No real solutions"
#		try again and let python return the complex numbers?
	if dis == 0: 
		return -b / (2*a)
	else: 
		x1 = (-b + math.sqrt(dis)) / 2*a
		x2 = (-b - math.sqrt(dis)) / 2*a
		return x1, x2
		
print(quadratic(3, 2, 1))
print(quadratic(6, 17, 12))
print(quadratic(1, -7, -3))
print(quadratic(1, 5, 6))
print(quadratic(-1, 4, -4))

# x= (-b +/- sqrt(b**2 - 4ac)/2a