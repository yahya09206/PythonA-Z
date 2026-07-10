def reverse_words_in_a_string(s:str) -> str:

	r = len(s) - 1
	words = []

	while r >= 0:

		while r >= 0 and s[r] == ' ':
			r -= 1

		if r < 0:
			break

		l = r
		while l >= 0 and s[l] != ' ':
			l -= 1

		words.append(s[l + 1: r + 1])

		r = l

	return ' '.join(words)


print(reverse_words_in_a_string("the sky is blue"))
print(reverse_words_in_a_string("  hello world  "))
print(reverse_words_in_a_string("a good   example"))