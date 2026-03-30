'''
Implement the following two functions:

remove_from_list(my_list: List[int], index: int) -> List[int]. It should remove the element at the given index from my_list and return the modified list.
pop_n_from_list(my_list: List[int], n: int) -> List[int]. It should pop the last n elements from my_list and return the modified list.
You may assume that the index given to remove_from_list will always be valid (i.e., it will be within the bounds of the list). You may also assume that the number of elements to pop from the list in pop_n_from_list will always be less than or equal to the length of the list.


'''

from typing import List # this is used to add type hints for List type

def remove_from_list(my_list: List[int], index: int) -> List[int]:
    
    my_list.pop(index)
    return my_list


def pop_n_from_list(my_list: List[int], n: int) -> List[int]:
    for i in range(n):
        my_list.pop()
    return my_list



# don't modify below this line
print(remove_from_list([1, 2, 3, 4, 5], 2))
print(remove_from_list([1, 2, 3, 4, 5], 0))
print(remove_from_list([1, 2, 3, 4, 5], 4))

print(pop_n_from_list([1, 2, 3, 4, 5], 2))
print(pop_n_from_list([1, 2, 3, 4, 5], 0))
print(pop_n_from_list([1, 2, 3, 4, 5], 5))
