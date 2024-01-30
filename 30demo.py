# 30demo.py by Adele Ferrer

#Loops

#i = 0
#while True:
#	i = i + 1
#	print('hey', i)
#	if i == 3: break
	
#i = 0
#while i < 3:
#	print(i)
#	i = i + 1
#print('final value of i is', i)

#for i in range(1, 10, 3):
#	print (i)
	
#for i in range(0, 5):
#	print (i)
	
#for i in range(5):
#	print (i)
	
#for char in 'hello':
#	print(char)
	
#seq = 'GAATTC'
#for nt in seq:
#	print (nt)

#for nt1 in 'ACGT':
#	for nt2 in 'ACGT':
#		if nt1 == nt2: print(nt1, nt2, '+1')		
#		else:          print(nt1, nt2, '-1')
		
nts = 'ACGT'
for nt1 in nts:
	for nt2 in nts:
		if nt1 == nt2: print(nt1, nt2, '+1')		
		else:          print(nt1, nt2, '-1')