sum_of_all_lines = 0
file = open("testinput.txt", "r")
for lines in file:
	first_digit = None
	last_digit = None

	for char in lines:
		if char.isdigit():
			if last_digit == None:
				last_digit = char
			first_digit = char
		sum_of_all_lines += int(first_digit) + (int(last_digit) * 10)

print(sum_of_all_lines)