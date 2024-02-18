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

hexd = []
mind = 1000
with open(colors) as fp:
	for line in fp:
		words = line.split('\t')
		color = words[0]
		dec = words[2].split(',')
		r = int(dec[0])
		g = int(dec[1])
		b = int(dec[2])
#		print(r, g, b)
		d = abs(R -r ) + abs(G -g) + abs(B- b)
		if d <mind:
			mind = d
			result = color
print(result)
#		print(color, abs(R -r )+ abs(G -g) + abs(B - b))


