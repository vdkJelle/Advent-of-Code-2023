sum_of_all_lines = 0
file = open("testinput.txt", "r")

def assign_digit(digit):
	global first_digit, last_digit

	if first_digit == None:
		first_digit = digit
	last_digit = digit

def strncmp(s1, s2, n):
	return s1[:n] == s2[:n]

for lines in file:
	first_digit = None
	last_digit = None
	index = 0

	while index < len(lines):
		char = lines[index]

		if char.isdigit():
			assign_digit(char)
		elif strncmp(lines[index:], "one", 3):
			assign_digit(1)
		elif strncmp(lines[index:], "two", 3):
			assign_digit(2)
		elif strncmp(lines[index:], "three", 5):
			assign_digit(3)
		elif strncmp(lines[index:], "four", 4):
			assign_digit(4)
		elif strncmp(lines[index:], "five", 4):
			assign_digit(5)
		elif strncmp(lines[index:], "six", 3):
			assign_digit(6)
		elif strncmp(lines[index:], "seven", 5):
			assign_digit(7)
		elif strncmp(lines[index:], "eight", 5):
			assign_digit(8)
		elif strncmp(lines[index:], "nine", 4):
			assign_digit(9)
		index += 1
	if first_digit is not None and last_digit is not None:
		sum_of_all_lines += (int(first_digit) * 10) + int(last_digit)

file.close()

print(sum_of_all_lines)
