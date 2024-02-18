# 53genomestats.py by Adele Ferrer

# sort then put into a list
# then return stats/ mean of list 

#if it has' ' around it, it's a string 
# without them it is a number/integer
# in order to do things w/ em, we want em to be integers
'''
for medians vals = [list of values]
	val[len(val)//2] #index to the middle values
	#Don't use this way? this way is "dirty"
'''
import gzip
import sys

gffpath = sys.argv[1]
feature = sys.argv[2]

val  = [] 
with gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		words = line.split()
		if words[2] == feature:
			begin = int(words[3])
			end = int(words[4])
			val.append(end - begin + 1)

val.sort() 

#Count
print(f'Count: {len(val)}')

#Minimum
print(f'Minimum: {val[0]}')

#Maximum
print(f'Maximum: {val[len(val) -1]}')

#Mean
total = 0
for x in val:
	total += x
mean = total /len(val)
print(f'Mean: {mean}')

#Standard Deviation
num = 0
for x in val:
	num += (x-mean)**2
variance = num / len(val)
st_dev = variance**0.5
print(f'St Dev: {st_dev}')

#Median
if len(val) % 2 == 0: #then checking if list length is odd or even
	med = (val[len(val)//2] + val[(len(val)//2) - 1]) /2  #need to take average of 2 mid values 
else:
	med = val[len(val)//2]
print(f'Median: {med}')


