def reverse_range(s, l , r):

	while l < r:
		s[l], s[r] = s[r], s[l]

		l += 1
		r -= 1


def reverse_string_iii(s:str):

	chars = list(s)
	start = 0
	n = len(chars)

	for end in range(n):

		if chars[end] == " " or end == n - 1:

			if end == n - 1:
				right_bound = end
			else:
				right_bound = end - 1

			reverse_range(chars, start, right_bound)

			start = end + 1

	return "".join(chars)


s1 = "Let's take LeetCode contest"
print(reverse_string_iii(s1))
