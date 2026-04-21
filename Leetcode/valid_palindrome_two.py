def is_palindrome(s,l,r):

	while l < r:


		if s[l] != s[r]:
			return False

		l += 1
		r -= 1

	return True

def valid_palindrome_two(s):

	l = 0
	r = len(s) - 1

	while l < r:

		if s[l] == s[r]:
			l += 1
			r -= 1

		else:
			return is_palindrome(s, l + 1, r) or is_palindrome(s, l, r - 1)

	return True



word = "aba"
word2 = "abc"

print(valid_palindrome_two(word))
print(valid_palindrome_two(word2))