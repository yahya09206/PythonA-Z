def backspace_compare(s:str, t:str) -> bool:

	l = len(s) - 1
	r = len(t) - 1
	l_skip = 0
	r_skip = 0

	while l >= 0 or r >= 0:

		while l >= 0 and (s[l] == "#" or l_skip > 0):
			if s[l] == "#":
				l_skip += 1
			else:
				l_skip -= 1

			l -= 1

		while r >= 0 and (t[r] == "#" or r_skip > 0):
			if t[r] == "#":
				r_skip += 1
			else:
				r_skip -= 1

			r -= 1

		if (l >= 0 and r < 0) or (r >= 0 and l < 0):
			return False

		if l >= 0 and r >= 0:
			if s[l] != t[r]:
				return False

		l -= 1
		r -= 1

	return True






	# result = []
	# result2 = []

	# for char in s:
	# 	if char.isalpha():
	# 		result.append(char)
	# 	elif char == '#' and len(result) > 0:
	# 		result.pop()

	# for char in t:
	# 	if char.isalpha():
	# 		result2.append(char)
	# 	elif char == '#' and len(result2) > 0:
	# 		result2.pop()

	# return result == result2

print(backspace_compare("ab#c", "ad#c"))
print(backspace_compare("ab##", "c#d#"))
print(backspace_compare("a#c", "b"))