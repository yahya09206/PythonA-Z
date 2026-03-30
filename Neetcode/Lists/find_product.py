def find_product(arr:List[int]) -> int:

	result = 1

	for i in range(len(arr)):

		result *= arr[i]
	return result

print(find_product([2,2,2]))
print(find_product([3,3,3]))