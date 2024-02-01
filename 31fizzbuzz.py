# 31fizzbuzz.py by Adele Ferrer

for i in range (1,16): #change range before turn-in
	if  i % 15 == 0: print('FizzBuzz')# needs to be first to override the 3 and 5 
	elif i % 3 == 0: print('Fizz')
	elif i % 5 == 0: print('Buzz')
	else:        print(i)
	
