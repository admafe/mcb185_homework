# sort then put into a list
# then return stats/ mean of list 

'''
for medians vals = [list of values]
	val[len(val)//2] #index to the middle values
	#Don't use this way? this way is "dirty"
'''

import sys

val  = []

for x in sys.argv[1:]:
	val.append(int(x))
print(val)

val.sort() #first thing is to sort list
print(val)

if len(val) % 2 == 0: #then checking if list **length** is odd or even
	med = val[((-len(val)//2) + (len(val)//2)) / 2] #need to take average of 2 mid values 
else:
	med = val[len(val)//2]
print(med)

#if it has' ' around it, it's a string 
# without them it is a number/integer
# in order to do things w/ em, we want em to be integers


