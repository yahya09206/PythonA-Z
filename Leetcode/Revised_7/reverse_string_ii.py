def reverse_helper(s, l, r):

	while l < r:

		s[l], s[r] = s[r], s[l]

		l += 1
		r -= 1


def reverse_string_two(s, k):

	chars = list(s)

	for i in range(0, len(s), 2 * k):

		l = i
		r = min(i + k - 1, len(s) - 1)

		reverse_helper(chars, l, r)

	return "".join(chars)