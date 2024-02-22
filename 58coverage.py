# 58coverage.py 
#In Class Practice for Unit 5 (2/20)
#Same logic as 57 birthday prob
#Thematically Unit 5, preview Unit 6 

import sys
import random

c_size = int(sys.argv[1])
r_size = int(sys.argv[2])
r_num = int(sys.argv[3])

#Create an empty chromosome 
chrom = []
for i in range(c_size):
	chrom.append(0)
	
#Fill it up with reads
#Still a 'For i' b/c it's still at same level of thought
#not inside other one
for i in range(r_num):
	pos = random.randint(0, c_size - r_size)
	for j in range(r_size):
		chrom[pos + j] += 1
	print(pos)
print(chrom)

#Find min coverage
min = r_num
for n in chrom[r_size:-r_size]:
	if n < min: min = n
#print(min)

#Window across each value
'''
for i in range(0, c_size - r_size +1):
	print(chrom[i: i + r_size])
'''
k = 15	
seq = 'ACGTACGTACGCTCAGTAGCG'
print(seq)
for i in range(0, len(seq) - k +1, 1): #adding 3 makes it trsltn, not trxn
	win = seq[i:i+k]
	g = win.count('g')
	c = win.count('C')
	print(i, win, g + c / k)
#	print(win)
#	print(seq[i: i + k])
	
# for 61, do this, count GC comp of each window

