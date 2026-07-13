def backspace_compare(s:str, t:str) -> bool:

	result = []
	result2 = []

	for char in s:
		if char.isalpha():
			result.append(char)
		elif char == '#' and len(result) > 0:
			result.pop()

	for char in t:
		if char.isalpha():
			result2.append(char)
		elif char == '#' and len(result2) > 0:
			result2.pop()

	return result == result2


print(backspace_compare("ab#c", "ad#c"))