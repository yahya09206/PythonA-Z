def reverse_range(chars, left, right):

	 while left < right:

	 	chars[left], chars[right] = chars[right], chars[left]
	 	left += 1
	 	right -= 1

def reverse_words(s: str) -> str:

    res = list(s)
    start = 0
    
    for end in range(len(res)):
        if res[end] == " ":
            reverse_range(res, start, end - 1)
            start = end + 1
        elif end == len(s) - 1:
            reverse_range(res, start, end)
            
    return "".join(res)


s1 = "Let's take LeetCode contest"
print(reverse_words(s1))