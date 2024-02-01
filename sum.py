# sum.py by Adele Ferrer
# In Class Examples (2/1/2024)

"""
s = 'n'
print(ord(s))
"""

def chksum(s):
	n = 0 #initialization
	for c in (s): #iteration
		n = n + ord(c)
	return n % 256 #finalization
	
#print(chksum('addie'))
#print(chksum('iankorf'))
		
"""
md5 <file name>
returns check sum for file
can be used to check if people have same file exactly or diff copies
"""
def maxchar(s):
	mx = 0 # set low initial condition for max
	for c in s:
		if ord(c) > mx: mx = ord(c)		
	return mx
	
def minchar(s):
	mn = 256 # set high initial condition for min 
	for c in s:
		if ord(c) < mn: mn = ord(c)
	return mn

import math
def euler(limit):
	e = 0
	for n in range(limit):
		e = e + 1 / math.factorial(n)
		print (e)
	return e
#print(euler(20))

# when naming boolean fxns add "is" to name (Ex: "is_perfect_square")
# use is_'condition' as name for boolean fxn

def is_perfect_square(n):
	root = math.sqrt(n)
	if root == root // 1: return True
	else: return False #This is a redundant statement;automatically if not true, is false
	
def is_prime(n):
	for den in range(2, n//2):
		if n % den == 0: return False #short circuit, cuts out of fxn if cond is met
		return True 
		
"""
name = 'addie'
print(chksum(name))
print(maxchar(name))
print(minchar(name))
"""

limit = 5
for i in range(1, limit): #don't need 0 values, so start at 1 
	for j in range(1, limit): 
		if i != j: #this is how you exclude major diagonal from whole matrix
	#i starts range at current value of first loop (ex:1,1 ; 2,2)
			print(i, j, 'c')
		
#full matrix = initialized at same thing 
# half matrix = initialize second loop at i of first loop
# half matrix - major diagonal = excludes comparisons against itself (1x1)
#	initialize second loop at i + 1, goes to next value 
# full matrix - major diagonal = 3rd loop? 
