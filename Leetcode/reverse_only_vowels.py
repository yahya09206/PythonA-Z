def reverse_vowels(s: str) -> str:

	chars = list(s)
	vowels = "aeiouAEIOU"
	l = 0
	r = len(chars) - 1

	while l < r:

		while l < r and chars[l] not in vowels:
			l += 1

		while l < r and chars[r] not in vowels:
			r -= 1

		chars[l], chars[r] = chars[r], chars[l]

		l += 1
		r -= 1

	return "".join(chars)


print(reverse_vowels("IceCreAm"))
print(reverse_vowels("leetcode"))