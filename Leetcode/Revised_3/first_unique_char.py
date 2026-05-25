def first_unique(s:str) -> int:

	count_map = {}

	for char in s:

		count_map = count_map.get(char, 0) + 1

	for i, char in enumerate(strs):

		if count_map[char] == 1:

			return i 

	return -1

