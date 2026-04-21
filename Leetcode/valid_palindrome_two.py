def is_palindrome(s,l,r):

	while l < r:


		if s[l] != s[r]:
			return False

		l += 1
		r -= 1

	return True

def valid_palindrome_two():

	

