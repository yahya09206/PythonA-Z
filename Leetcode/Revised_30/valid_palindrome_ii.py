def valid_palindrome(s, l, r):

	while l < r:

		if s[l] != s[r]:
			return False

		l += 1
		r -= 1

	return True


def valid_palindrome_ii(s):

	l = 0
	r = len(s) - 1

	while l < r:

		if s[l] == s[r]:
			l += 1
			r -= 1
		else:
			return valid_palindrome(s, l + 1, r ) or valid_palindrome(s, l, r - 1)

	return True


word = "aba"
word2 = "abc" 

print(valid_palindrome_ii(word))
print(valid_palindrome_ii(word2))