# 35nchoosek.py by Adele Ferrer

def factorial(n):
	if n == 0: return 1
	for i in range(1, n):
		n = n * i
	return(n)

def nchoosek(n, k):
	return(factorial(n) / (factorial(k) * factorial(n - k)))
	
print(nchoosek(5, 2))
print(nchoosek(10, 4))
print(nchoosek(26, 8))