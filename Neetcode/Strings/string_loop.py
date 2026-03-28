'''
Implement a function called print_string_characters(my_string: str) -> None. 
It takes a string as a parameter and prints each character of the string separately.
'''
def print_string_characters(my_string: str) -> None:

    for i in range(len(my_string)):
    	print(my_string[i])


# do not modify below this line
print_string_characters("Hello, World!")
print_string_characters("Good Job!")