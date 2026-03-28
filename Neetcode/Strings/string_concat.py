'''
Implement the function concatenate(s1: str, s2: str) -> str. 
It accepts two strings as parameters and returns a new string that is the concatenation of the two input strings. 
If the length of the string after concatenating them is greater than 10, return "Too long!".

For example,

If you call concatenate("Good ", "job!"), it should return "Good job!".
If you call concatenate("Goodbye, ", "world!"), it should return "Too long!".
'''

def concatenate(s1: str, s2: str) -> str:
	if len(s1) + len(s2) <= 10:
		return s1 + s2
    return "Too long!"



# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
