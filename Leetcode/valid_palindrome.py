def valid_palindrom(s:str) -> bool:
	
	l = 0
	r = len(s) - 1

	while l < r:

		while l < r and not s[l].isalnum():
			l += 1

		while l < r and not s[r].isalnum():
			r -= 1

		if s[l].lower() != s[r].lower():
			return False

		l += 1
		r -= 1

	return True



s1 = "racecar"
s2 = "A man, a plan, a canal: Panama"
s3 = "race a car"
s4 = ".,"
print(valid_palindrom(s1))
print(valid_palindrom(s2))
print(valid_palindrom(s3))
print(valid_palindrom(s4))