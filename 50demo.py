# 50demo.py by Adele Ferrer

'''
seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1]) #does it backwards
'''

#Tuples
'''
tax = ('Homo', 'sapiens', 9606) 
print(tax)
'''
# tuples made with parenthesis

#tax[0] = '1'

def quadratic(a, b, c):
    x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    return x1, x2

'''
x = quadratic(1,1,1)
print(x[1]) #prints it as a tuple, 2 values in one variable 


#Unpacked tuple
x1, x2 = quadratic(1,2,3) 
print(x2)
# assignments for each one, unpacked 
'''


#How to index a tuple
'''
nts = 'ACGTN'
for i in range(len(nts)):
	print(i, nts[i])

#best/simplest way to do it	
for i, nt in enumerate(nts): #gives the index values and the values in tuple
	print(i, nt)

#worst way to do it, redundant 	
i = 0
for nt in nts:
	print(i, nt)
	i += 1	

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for nt, name in zip(nts, names): #zip allows enumeration without items being same length
	print(nt,name)
'''

#Tuple for variables, for known length things
#Lists for items of unknown lengths 

#Lists: allows you to change items in list 

nts =['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)