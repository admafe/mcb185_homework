# 33triples.py by Adele Ferrer

#just need integer test for c value output 
#use an if and a boolean 

# if c == c //1
# is integer 

#Needs loop inside a loop; nested loop 
"""
def triples(a, b):
	if a**2 + b**2 == c**2:
		if c == c//1:
			return (c)
	
"""
"""	
print(is_triples(3, 4, 5)) #yes
print(is_triples(1, 2, 3))
print(is_triples(5, 12, 13)) #yes
print(is_triples(4, 7, 12))
"""

import math

limit = 100
for a in range(1, limit): 
	for b  in range(a + 1, limit): 
		c = math.sqrt(a**2 + b**2)
		if c == c//1: print(a, b, c)
if a != b: print(a, b, c)
			
