def reverse(s, l, r):

	while l < r:

		s[l], s[r] = s[r], s[l]
		l += 1
		r -= 1


def reverse_string_iii(s:str) -> str:

	chars = list(s)
	start = 0

	for end in range(0, len(chars)):

		if chars[end] == " " or end == len(chars) - 1:

			l = start

			if end == len(chars) - 1:
				r = end
			else:
				r = end - 1

			reverse(chars, start, r)

			start = end + 1



	return "".join(chars)


s1 = "Let's take LeetCode contest"
print(reverse_string_iii(s1))


# s'teL ekat edoCteeL tsetnoc