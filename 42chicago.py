# 42chicago.py by Adele Ferrer

import random

zero_games = 0 
total_score = 0
games_played = 100000
for i in range(games_played):
	score = 0
	for roundnum in range(2, 13):
#		print(roundnum)
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 + d2 == roundnum:
			score += roundnum
		
#	print(score)
	total_score += score
	if score == 0:
		zero_games += 1
		
print(zero_games / games_played)
print(total_score / games_played)
	
# use pipe commands in term to count stats of things 
# sort -n | uniq -c | sort -n
		
		