def valid_anagram(s:str, t:str) -> bool:

	count_map = {}

	for char in s:

		count_map[char] = count_map.get(char, 0) + 1

	for char in t:

		count_map[char] = count_map.get(char, 0) - 1

	for count in count_map.values():
		if  count != 0:
			return False

	return True


print(valid_anagram("anagram", "nagaram"))
print(valid_anagram("rat", "car"))