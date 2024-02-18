# 56birthday.py by Adele Ferrer
'''
finding duplicates within a set of data
in diff group sizes

you're collecting the birthdays 
sort them then compare? 
then code for finding duplicates with in that list of birthdays 
half matrix minus major diagonal:
compare everything to everything else w/out comparing to self 

1: Get all the birthdays
	a: half matrix it 
	b: sort; then look for duplicates
2: Check as you go/ as list builds (same as half mat but simultaneous) **Faster**
	
3: Sort into bins by month...? , when a certain month goes up in count of 1, stop
(Basically create a calendar) #57
'''
import random
import sys

#trials = int(sys.argv[1])
#days = int(sys.argv[2])
people = int(sys.argv[1])

birthdays = []
for i in range(people):
	month = random.randint(1,12)
	if month == 4 or month == 6 or month == 9 or month == 11:
		day = random.randint(1,30)
	elif month == 2:
		day = random.randint(1,28)
	else: 
		day = random.randint(1,31)
	birthday = f'{month}/{day}'
	birthdays.append(birthday)
	
#print(birthdays)
