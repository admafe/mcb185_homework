# 37nilakantha.py by Adele Ferrer

def nilakantha(n):
	x = 3
	for i in range(2, n, 3):
		denom = (i) * (i + 1) * (i + 2)
		if i%2 == 0: return(+denom)
		else:        return((-1)*denom)
	pi = x + (4/denom)
	return (pi)
		
print(nilakantha(5))
print(nilakantha(21))
	
# set range, flip flop, for every even = +
# for every odd = -
"""	
if i%2 == 0: +
if i%2 == 1: -
"""