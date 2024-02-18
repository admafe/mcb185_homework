# 50demo.py by Adele Ferrer

'''
seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1]) #does it backwards
'''

#Tuples
'''
tax = ('Homo', 'sapiens', 9606) 
print(tax[0]) #index
print(tax[::-1])#slice
'''
#Slices

s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#print(s[::-1]) #-1 prints the string backwards

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

'''
nts =['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

last = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse =True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)
'''

#Creating empty lists, then adding things to them
'''
items = list()
print(items)
items.append('eggs')

stuff = []
stuff.append(3)
print(stuff)
print(items)
'''
'''
alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)

text = 'good day    to you'
words = text.split()

line = '1.42,2.72,3.14'
print(line.split(',')) #use for tsv or csv data

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)
print(words)

#using 'in' for item in container
if 'A' in alph: print('yay')
if 'a' in alph: print('no')

#indexing a container
print('index G?', alph.index('G'))
#print('index Z?', alph.index('Z')) #shows an error, there is no Z in alph

#finding something in container
print('find G?', alph.find('G')) # returns value of item in list that matches
print('find Z?', alph.find('Z')) #returns -1 since Z not found
'''
#Practice
'''
import sys

values = []

#def min():
for x in sys.argv[1:]:
	values.sort(int(x))
print(values)
'''
'''
vals =[1, 4, 5, 7, 2, 9]

def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini
	
print(minimum(vals))
'''

