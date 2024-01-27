#20demo.py by Adele Ferrer

print ('hello, again') #greeting 
"""
This is a
multi-line
comment
"""
#Test Math 
import math

#print(1.5e-2)
#print(5%2)
#print(5//2)
#print(2**3)
#print(math.sqrt(2))
#print(math.ceil(37.5))
#print(math.pi)
#print(math.inf)
#print(pow(2,3))

#Variables

#a=3
#b=4
#c= math.sqrt(a**2 + b**2)
#print(c)

#print(type(a), type(b), type(c))
#print(type(a), type(b), type(c), sep=", ")

#Functions

#def greeting():
#	print('hello yourself')
#greeting()
	
#def pythagoras(a, b):
	#return math.sqrt(a**2 + b**2)
	
#print(pythagoras(3,4))
#print(pythagoras(1,1))

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

#def inverse(a):
#	return -a
#print(inverse(-4))
#print(inverse(12))

#def triangle(a, b):
#	return (a*b)/2
#print(triangle(5, 12))

#def midpoint(x1, y1, x2, y2):
#	mx=(x1 + x2)/2
#	my=(y1 + y2)/2
#	return mx, my
#x, y = midpoint(4, 1, 10, 5)
#print(x, y)
	
#s = 'hello world'
#print(s, type(s))

#Conditionals
a = 0.3
b = 0.1 * 3

if a != b:
	print('a does not equal b')
if a == b:
	print('a equals b')
print(a, b)

c = a == b
print(c)
print(type(c))

if a < b:  print('a < b')
elif a > b:print('a > b')	
else:      print('a == b')

if a < b or a > b: print('a and b are not equal')
if a < b and a > b: print('what kinda world is this')
if not False: print(True)

if math.isclose(a, b): print('close enough')

s1 = 'a'
s2 = 'b'
s3 = 'a'
if s1 < s2: print('A < b')
if s2 < s3: print('B < a')

#a = 1
#s = 'G'
#if a < s: print('a < s')

a = 15
def odd(a):
	if 
	if not a/2: print('odd')
