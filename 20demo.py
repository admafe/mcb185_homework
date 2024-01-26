#20demo.py by Adele Ferrer
print ('hello, again') #greeting 
"""
This is a
multi-line
comment
"""
#Test Math 
import math

print(1.5e-2)
print(5%2)
print(5//2)
print(2**3)
print(math.sqrt(2))
print(math.ceil(37.5))
print(math.pi)
print(math.inf)
print(pow(2,3))

#Variables
a=3
b=4
c= math.sqrt(a**2 + b**2)
print(c)

print(type(a), type(b), type(c))
print(type(a), type(b), type(c), sep=", ")

#Functions
def greeting():
	print('hello yourself')
	
def pythagoras(a, b):
	return math.sqrt(a**2 + b**2)
	
print(pythagoras(3,4))
print(pythagoras(1,1))

#def pythagoras(a, b):
#	assert(a > 0)
#	assert(b > 0)
#	return math.sqrt(a**2 + b**2)
#print(pythagoras(-1, 1))

import sys
#def pythagoras(a, b):
#	if a <= 0: sys.exit('error: a must be greater than 0')
#	if b <= 0: sys.exit('error: b must be greater than 0')
#	return math.sqrt(a**2 + b**2)
#print(pythagoras(2,-4))

def inverse(a):
	return -a
print(inverse(-4))
print(inverse(12))
	
s = 'hello world'
print(s, type(s))