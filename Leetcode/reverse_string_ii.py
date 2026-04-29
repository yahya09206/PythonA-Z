def reverse_string_ii(s:str, k:int) -> str:

	# Step 1: Convert string to a mutable list (The "Binder")
	chars = list(s)
	n = len(chars)

	# Step 2: Jump through the list in blocks of 2k
	for i in range(0, n, 2 * k):

		# Step 3: Set our Opposite Ends pointers for the first k characters
		left = i

		# Use min() to ensure we don't fall off the end of the list
		right = min(i + k - 1, n - 1)

		# perform swap
		while left < right:
			chars[left], chars[right] = chars[right], chars[left]
			left += 1
			right -= 1

	# Step 5: Join the list back into a string
	return "".join(chars)



s1 = "abcdefg"
print(reverse_string_ii(s1, 2))






