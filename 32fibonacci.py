# 32fibonacci.py by Adele Ferrer

#need to set range, then add each number set, and loop through each new number

'''
#Work in progress
def fibonacci(n):
	n1 = 0
	n2 = 1
	for i in range(n):
		temp = n1 
		n = n + i
		for 
	return (n)
	
print(fibonacci(1))
print(fibonacci(9))
'''

#for i in range(0,21):
#	n1 = i
#	n2 = n2 + n1	
#	print(n2)

#Need a variable to hold first argument, then loop through that variable
# Check notes for more 

#need sequence for this? (seq = )

def fibonacci(n):
	n1 = 0
	n2 = 1
	for i in range(n):
		print(n1)
		temp = n1
		n1 = n2
		n2 = temp + n2

print(fibonacci(9))
#print(fibonacci(5))
#print(fibonacci(20))