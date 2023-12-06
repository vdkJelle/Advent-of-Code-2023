SPECIAL_CHARACTERS = "!@#$%^&*()-_=+/"
total_numbers_found = 0

# with open("smalltest.txt", "r") as file:
with open("testinput.txt", "r") as file:
	map = []

	for lines in file:
		row = list(lines.strip())
		map.append(row)

def find_special_character_around_element(map, x, y):
	num_rows = len(map)
	num_cols = len(map[0])

	if x > 0:
		if y > 0:
			if map[x - 1][y - 1] in SPECIAL_CHARACTERS:
				return True
		if map[x - 1][y] in SPECIAL_CHARACTERS:
			return True
		if y + 1 != num_cols:
			if map[x - 1][y + 1] in SPECIAL_CHARACTERS:
				return True
	if y > 0:
		if map[x][y - 1] in SPECIAL_CHARACTERS:
			return True
		if x + 1 != num_rows:
			if map[x + 1][y - 1] in SPECIAL_CHARACTERS:
				return True
	if y + 1 != num_cols:
		if map[x][y + 1] in SPECIAL_CHARACTERS:
			return True
	if x + 1 != num_rows:
		if map[x + 1][y] in SPECIAL_CHARACTERS:
			return True
		if y + 1 != num_cols:
			if map[x + 1][y + 1] in SPECIAL_CHARACTERS:
				return True
	return False

for x, row in enumerate(map):
	found_special_character = False
	temporary_number_storage = None

	for y, current_element in enumerate(row):
		if current_element.isdigit():
			if found_special_character is False:
				found_special_character = find_special_character_around_element(map, x, y)

			if temporary_number_storage is None:
				temporary_number_storage = int(current_element)
			else:
				temporary_number_storage = (temporary_number_storage * 10) + int(current_element)
		elif current_element.isdigit() is not True:
			if temporary_number_storage is not None and found_special_character is True:
				total_numbers_found += temporary_number_storage
			temporary_number_storage = None
			found_special_character = False
	if temporary_number_storage is not None and found_special_character is True:
		total_numbers_found += temporary_number_storage
		# print(f"({x}, {y}): {current_element}, Special: {found_special_character}, Total: {total_numbers_found}")


print(total_numbers_found)
