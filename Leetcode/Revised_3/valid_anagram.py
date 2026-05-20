'''
if strings have different lengths:
return False

create hashmap:
character → frequency

loop through first string:
add character counts

loop through second string:
subtract character counts

check all hashmap values:
if any value is not 0:
return False

return True
'''

def valid_anagram(s:str, t:str) -> bool:

	if len(s) != len(t):
		return False

	count_map = {}

	for char in s:
		count_map[char] = count_map.get(char, 0) + 1

	for char in t:
		count_map[char] = count_map.get(char, 0) - 1

	for val in count_map.values():
		if val != 0:
			return False

	return True
