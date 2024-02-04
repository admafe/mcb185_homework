# 37nilakantha.py by Adele Ferrer

def nilakantha(n):
	x = 3
	sign = 1
	
	for i in range(2, n, 3):
		denom = (i) * (i + 1) * (i + 2)
#		if i % 2 == 0: return(+denom)
#		else:        return((-1)*denom)
		estimate = (sign * (4/denom))
		sign = sign * -1
		x = estimate + x

	return (x)
		
print(nilakantha(5))
print(nilakantha(21))
print(nilakantha(1000000))
	
# set range, flip flop, for every even = +
# for every odd = -
"""	
if i%2 == 0: +
if i%2 == 1: -
"""