def reverse_string(str:List[String]) -> None:

	l = 0
	r = len(str) - 1

	while l < r:

		str[l], str[r] = str[r], str[l]
		l += 1
		r -= 1

	return str 


string = ["a", "b", "c"]
print(reverse_string(string))