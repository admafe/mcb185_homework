# 34scoringmatrix.py by Adele Ferrer

#just keep printing rows at a time and cut the ending so it doesn't go to new row
# use "end = " so it ends with space not return

nts = 'ACGT'
for nt1 in nts:
	nt1 = nt1 + 1
	print(nt1, end = ' ')
"""
	for nt2 in nts:
		if nt1 == nt2: print(nt1, nt2, '+1', end = ' ')		
		else:          print(nt1, nt2, '-1', end = ' ')
"""