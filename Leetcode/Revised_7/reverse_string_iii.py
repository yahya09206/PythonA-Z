def reverse_range(s, l, r):

	while l < r:

		s[l], s[r] = s[r], s[l]

		l += 1
		r -= 1