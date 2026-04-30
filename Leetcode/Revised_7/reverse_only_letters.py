def reverse_letters(s: str) -> str:

	chars = list(s)
	l = 0
	r = len(chars) - 1

	while l < r:

		while l < r and not chars[l].isalpha():
			l += 1
		while l < r and not chars[r].isalpha():
			r -= 1

		if l < r:
			chars[l], chars[r] = chars[r], chars[l]

			l += 1
			r -= 1

	return "".join(chars)


print(reverse_letters("Test1ng-Leet=code-Q!"))
print(reverse_letters("ab-cd"))
print(reverse_letters("a-bC-dEf-ghIj"))