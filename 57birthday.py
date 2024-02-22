# 57birthday.py by Adele Ferrer
# Co-Author: Marle Lamountry

#Same thing as 56 but do it by month, by calendar
#choose a random birthday, stick it in the calendar
#variable that will count how many birthdays in each month

import sys
import random

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

duplicates = 0
for i in range(trials):
	calendar = []
	for i in range(days):
		calendar.append(0)
	for j in range(people):
		birthday = random.randint(1, days - 1)
		calendar[birthday] += 1
		if calendar[birthday] > 1:
			duplicates += 1
			break

#print(calendar)
print(duplicates/trials)

'''
duplicates = 0
for i in range(trials):
	birthdays = []
	for j in range(people):
		if birthday in birthdays: 
			duplicates += 1
			break
		else:
			birthdays.append(birthday)
			
calendar = []
for i in range(people):
	birthday = random.randint(days)
	for j in range(1,12):
		calendar[birthday + j] += 1


'''
