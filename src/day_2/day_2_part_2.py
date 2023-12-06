import string
import re

sum_of_powers = 0
current_game_id = 1

def strncmp(s1, s2, n):
	return s1[:n] == s2[:n]

file = open("testinput.txt", "r")
for lines in file:
	subset_red = 0
	subset_green = 0
	subset_blue = 0
	subset_number = 0
	current_highest_red = 0
	current_highest_green = 0
	current_highest_blue = 0
	index = None	
	if current_game_id < 10:
		index = 8
	elif current_game_id < 100:
		index = 9
	else:
		index = 10

	while index < len(lines):
		char = lines[index]

		if char.isdigit():
			match = re.search(r'\b\d+\b', lines[index:])

			if match:
				subset_number = int(match.group())
				if subset_number > 9:
					index += 2
				else:
					index += 1
		elif strncmp(lines[index:], "red", 3):
			subset_red += subset_number
		elif strncmp(lines[index:], "green", 5):
			subset_green += subset_number
		elif strncmp(lines[index:], "blue", 4):
			subset_blue += subset_number
		elif char == ';':
			if subset_red > current_highest_red:
				current_highest_red = subset_red
			subset_red = 0
			if subset_green > current_highest_green:
				current_highest_green = subset_green
			subset_green = 0
			if subset_blue > current_highest_blue:
				current_highest_blue = subset_blue
			subset_blue = 0
		index += 1
	
	if subset_red > current_highest_red:
		current_highest_red = subset_red
	if subset_green > current_highest_green:
		current_highest_green = subset_green
	if subset_blue > current_highest_blue:
		current_highest_blue = subset_blue

	sum_of_powers += (current_highest_red * current_highest_green * current_highest_blue)
	current_game_id -= -1

print(sum_of_powers)