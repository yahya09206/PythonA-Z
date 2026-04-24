def reverse_only_letters(s:str) -> str:

	# Step 1: convert string to a list(since strings are immutable)
	chars = list(s)
	l = 0
	r = len(chars) - 1

	while l < r:
		# Step 2: Skip non-letters from the left
        # (Hint: Use a while loop + chars[l].isalpha())
        while l < r and not chars[l].isalpha():
        	l += 1
            
            
        # Step 3: Skip non-letters from the right
        while l < r and not chars[r].isalpha():
           	r -= 1

        # Step 4: Final check and swap(using tuple)
        if l < r:
           	chars[l], chars[r] = chars[r], chars[l]

           	# Move pointers after swapping
           	l += 1
           	r -= 1

        # Step 5: conver the list back into a string
    return "".join(chars)


print(reverse_only_letters("Test1ng-Leet=code!"))