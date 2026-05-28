def first_unique_char(s:str) -> int:

	count_map = {}

	for i, char in enumerate(s):

		count_map[char] = count_map.get(char, 0) + 1

	for i, char in enumerate(s):
		if count_map[char] == 1:
			return i  

	return -1


print(first_unique_char("leetcode"))
print(first_unique_char("loveleetcode"))