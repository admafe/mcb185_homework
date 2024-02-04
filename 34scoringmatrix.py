# 34scoringmatrix.py by Adele Ferrer
# Co-author: George M

# just keep printing rows at a time 
# cut the ending so it doesn't go to new row
# use "end = " so it ends with space not return

nts = 'ACGT'

for nt in nts: 
	if nt == 'A': print('  ', nt, end = '  ')
	else: print(nt, end = '  ')
print() #for loop for title line

for nt1 in nts:
	print(nt1, end = ' ') #print nt at beginning of each loop/ line
	for nt2 in nts:
		if nt1 == nt2: print('+1', end = ' ')		
		else:          print('-1', end = ' ')
	print() #print new line at each loop end
