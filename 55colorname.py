# 55colorname.py by Adele Ferrer

#finding min in list of values 

'''
read in file
split it to columns you want
then sort the min
'''

import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

min_dist = 1000
with open(colorfile) as fp:
	for line in fp:
		words = line.split('\t')
		col_name = words[0]
		dec = words[2].split(',')
		r = int(dec[0])
		g = int(dec[1])
		b = int(dec[2])
#		print(r, g, b)
		dist = abs(R - r) + abs(G - g) + abs(B - b)
		if dist < min_dist:
			min_dist = dist
			result = col_name
			
print(result)
#print(result, dist)


