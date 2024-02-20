# 30demo.py by Adele Ferrer

#Loops
'''
i = 0
while True:
	i = i + 1
	print('hey', i)
	if i == 3: break

i = 0
while i < 3:
	print(i)
	i = i + 1
print('final value of i is', i)


for i in range(1, 10, 3): #3 gets used when reading nucleotides, frames of 3
	print (i)
		
for i in range(0, 5):
	print (i)
	
for i in range(5):
	print (i)
	
for char in 'hello':
	print(char)
	
seq = 'GAATTC'
for nt in seq:
	print (nt)

for nt1 in 'ACGT':
	for nt2 in 'ACGT':
		if nt1 == nt2: print(nt1, nt2, '+1')		
		else:          print(nt1, nt2, '-1')
	#use for scoring matrix!!!!!
'''	
'''
nts = 'ACGT'
for nt1 in nts:
	for nt2 in nts:
		if nt1 == nt2: print(nt1, nt2, '+1')		
		else:          print(nt1, nt2, '-1')
# full scoring matrix
'''

'''	
limit = 4
for i in range(0, limit):
	for j in range(i +1, limit):
		print(i+1, j+1)
'''
# half scoring matrix, starts at i +1, goes to next loop, so no a*a
'''
def gc_comp(seq):
	gc_count = 0
	total = 0 
	for nt in seq:
		if nt == 'C' or nt == 'G':
			gc_count = gc_count + 1
		total = total + 1
	return gc_count / total 
	
print(gc_comp('ACAGCGAAT'))
'''


#Practice Problems 
# 1 is a for loop
# 2 is also a for loop
# 	need if argument for factorial of 0 which = 1
# 3 uses the factorial from 2
# 4 is a boolean?, function, 
# 5 test to divide i by half of numbs below it 
# what does it mean to be prime? define. 
#	(Ex: 45/ 1,2,3,..22)

def factorial(n):
	if n == 0: return 1
	for i in range(1, n):
		n = n * i
	return(n)

print(factorial(5))
print(factorial(12))
print(factorial(0))
		
	