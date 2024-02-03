# 36poisson.py by Adele Ferrer

import math

def factorial(n):
	if n == 0: return 1
	for i in range(1, n):
		n = n * i
	return(n)

def poisson(n, k):
	p = ((n**k) * (math.e ** (-n))) / factorial(k)
	return(p)
	
print(poisson(2, 4)) # should be about 0.0902
print(poisson(7, 17))
print(poisson(1, 1))

#Ask about the formula in the repo compared to poisson formula on internet