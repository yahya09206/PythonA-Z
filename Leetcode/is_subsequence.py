def is_subsequence(s:str,t:str) -> bool:

	l = 0
	r = 0

	while l < len(s) and r < len(t):
		if s[l] == t[r]:
			l += 1

		r += 1

	return l == len(s)

	# last_found_index = -1

	# for char in s:
	# 	found = False

	# 	for j in range(last_found_index + 1, len(t)):
	# 		if t[j] == char:
	# 			last_found_index = j
	# 			found = True
	# 			break

	# 	if not found:
	# 		return False

	# return True


print(is_subsequence("abc", "ahbgdc"))
print(is_subsequence("axc", "ahbgdc"))