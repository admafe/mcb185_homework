# 46savingthrows.py by Adele Ferrer

import random

#code function for each roll type (makes pretty/clean)

# Normal Roll
def normal(): 
	roll = random.randint(1, 20)
	return roll
#print(normal())	

# Advantage Roll (keep greater dice)
def advantage(): 
	d1 = random.randint(1, 20)
	d2 = random.randint(1, 20)
#	print(d1, d2)
	if d2 < d1: roll = d1
	else:       roll = d2
	return roll
#print(advantage())

# Disadvantage Roll (keep lesser dice)
def disadvantage():
	d1 = random.randint(1, 20)
	d2 = random.randint(1, 20)
#	print(d1, d2)
	if d2 < d1: roll = d2
	else:       roll = d1
	return roll
#print(disadvantage())
	
# create a for loop for trials 

#have to call each function again and again for each type of roll
#so same but for dis and adv 

trials = 10000

# Normal Rolls
for dc in range(5, 16, 5):
	print(f'Difficulty {dc}') 
	
	successes = 0
	for i in range(trials):
			n_roll = normal()
			if n_roll >= dc: successes += 1
	print(f'Normal {successes / trials}')
	
	successes = 0
	for i in range(trials):
			a_roll = advantage()
			if a_roll >= dc: successes += 1
	print(f'Advantage {successes / trials}')
	
	successes = 0
	for i in range(trials):
			d_roll = disadvantage()
			if d_roll >= dc: successes += 1
	print(f'Disadvantage {successes / trials}')
