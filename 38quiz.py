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
		
#print(pi_estimate(16))
#print(pi_estimate(100))

#Task 2
def nilakantha(n):
	x = 3
	sign = 1
	for i in range(2, n, 3):
		denom = (i) * (i + 1) * (i + 2)
		estimate = (sign * (4/denom))
		sign = sign * -1
		x = estimate + x
	return (x)
	
#def(simulataneous)

print(pi_estimate(100), nilakantha(100))