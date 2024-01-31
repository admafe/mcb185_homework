# 22oligotemp.py by Adele Ferrer

def oligotemp(a, c, g, t):
	oligo = a + c + g + t
	if oligo <= 13: tm = 2 * (a + t) + 4 * (g + c) 
	elif oligo > 13: tm = 64.9 + 41 * (g + c - 16.4) / oligo
	return tm 
	
print(oligotemp(1, 2, 2, 1))
print(oligotemp(7, 4, 3, 2))
print(oligotemp(18, 22, 27, 32))


