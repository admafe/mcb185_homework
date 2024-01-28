# 22oligotemp.py by Adele Ferrer

def oligotemp(A, C, G, T):
	oligo = A + C + G + T
	if oligo <= 13: tm = 2 * (A + T) + 4 * (G + C) 
	elif oligo > 13: tm = 64.9 + 41 * (G + C - 16.4) / oligo
	return tm 
	
print(oligotemp(1,2,2,1))
print(oligotemp(7, 4, 3, 2))
print(oligotemp(18, 22, 27, 32))