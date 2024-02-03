# 33triples.py by Adele Ferrer

#just need integer test for c value output 
#use an if and a boolean 

# if c == c //1
# is integer 

#Needs loop inside a loop; nested loop 

def is_triples(a, b, c):
	if a**2 + b**2 == c**2:
		if c == c//1:
			return True
	else: return False 
	
print(is_triples(3, 4, 5))
print(is_triples(1, 2, 3))
print(is_triples(5, 12, 13))
print(is_triples(4, 7, 12))