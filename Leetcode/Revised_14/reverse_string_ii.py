def reverse_range(s, l, r):

	while l < r:
		s[l], s[r] = s[r], s[l]

		l += 1
		r -= 1


def reverse_string(s:str, k:int) -> str:

	chars = list(s)
	n = len(s)

	for i in range(0, n, 2*k):

		l = i
		r = min(i + k - 1, n - 1)

		reverse_range(chars, l, r)


	return "".join(chars)

s1 = "abcdefg"
print(reverse_string(s1, 2))

