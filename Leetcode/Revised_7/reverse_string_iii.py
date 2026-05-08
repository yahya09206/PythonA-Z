def reverse_range(s, l, r):

	while l < r:

		s[l], s[r] = s[r], s[l]

		l += 1
		r -= 1


def reverse_string_three(s:str) -> str:

	chars = list(s)
	start = 0

	for end in range(0, len(chars)):

		if chars[end] == " " or end == len(chars) - 1:

			if end == len(chars) - 1:
				r = end
			else:
				r = end - 1

			reverse_range(chars, start, r)

			start = end + 1

	return "".join(chars)

