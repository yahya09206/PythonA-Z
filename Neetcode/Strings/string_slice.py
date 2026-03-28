'''
Implement a function called get_substring(input_string: str, start: int, end: int) -> str. 
It takes a string and two integers as parameters, 
and returns the substring of input_string string from the start index to the end index (not including the end index).

Important: If end is an invalid index, return an empty string. 
You may assume that start will always be a valid index and that end will always be greater than or equal to start.

The last valid index for a slice is the length of the string. Remember that
end is not included for a slice. The last character included will be at index
end - 1.

'''

def get_substring(input_string: str, start: int, end: int) -> str:

	if end > len(input_string):
		return ""
	return input_string[start:end]





# do not modify below this line
print(get_substring("NeetCode", 1, 7))
print(get_substring("NeetCode", 1, 8))
print(get_substring("NeetCode", 1, 9))
print(get_substring("NeetCode", 0, 2))
print(get_substring("NeetCode", 0, 7))
print(get_substring("NeetCode", 4, 8))
