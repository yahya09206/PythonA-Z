def count_even(arr:List[int]) -> int:

	count = 0

	for i in range(len(arr)):
		if arr[i] % 2 == 0:
			count += 1
	return count 

print(count_even([1,2,2,3,4]))