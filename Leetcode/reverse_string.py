from typing import List

def reverse_string(str: List[String]) -> None:

	l = 0
	r = len(str) - 1

	while l < r:
		temp = str[l]
		str[l] = str[r]
		str[r] = temp
		l += 1
		r -= 1
	return str  

string = ["a", "b", "c"]
print(reverse_string(string))