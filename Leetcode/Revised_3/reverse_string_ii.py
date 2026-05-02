def reverse_string_ii(s:str, k:int) -> str:

	chars = list(s)
	n = len(chars)

	for i in range(0, n, 2 * k):

		l = i

		r = min(i + k - 1, n - 1)

		while l < r:
			chars[l], chars[r] = chars[r], chars[l]
			l += 1
			r -= 1
	return "".join(chars)


s1 = "abcdefg"
print(reverse_string_ii(s1, 2))

