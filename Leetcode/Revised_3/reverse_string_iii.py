# --- THE HELPER METHOD ---
def reverse_helper(chars, left, right):

	while left < right:
		chars[left], chars[right] = chars[right], chars[left]
		left += 1
		right -= 1


def reverse_words(s: str) -> str:

	# 1. Convert to list since strings are immutable
	res = list(s)

	# 2. capture length of list in a variable
	n = len(res)
	start = 0

	# 3. Main loop will scan for the space at the end or the end of the length. Name "end"
	for end in range(n):

		# Handle if a space or end of list is found
		if res[end] == " " or end == n - 1:

			# 4. define boundary on where the end pointer should be
			# if the end pointer is at the end of the string then set the right pointer to the last index
			if end == n - 1:
				right_bound = end
			# else set it to the first word to the left of the string
			else:
				right_bound = end - 1

			# 5. insert swap logic
			reverse_helper(res, start, right_bound)

			# 6. move starting index to the beginning of the next word which
			# would be on the opposite side of the space
			start = end + 1

	# 7. Return reversed string
	return "".join(res)




s1 = "Let's take LeetCode contest"
print(reverse_words(s1))

