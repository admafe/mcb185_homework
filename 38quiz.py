# 38quiz.py by Adele Ferrer
# Co-author: Marle Lamountry

#Task 1
def pi_estimate(n):
	x = 1
	sign = -1
	for n in range(3, n, 2): 
		y = (sign * (1 / n))
		x = x + y
		sign = sign * -1
		pi = 4 * (x)
	return(pi)
		
print(pi_estimate(16))
print(pi_estimate(100))

#Task