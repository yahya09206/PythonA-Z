def valid_anagram(s:str, t:str) -> bool:

	if len(s) != len(t):
		return False

	count_map = {}


	for i, char in enumerate(s):
		count_map[char] = count_map.get(char, 0) + 1

	for j, char in enumerate(t):
		count_map[char] = count_map.get(char, 0) - 1


	for val in count_map.values():
		if val != 0:
			return False

	return True


