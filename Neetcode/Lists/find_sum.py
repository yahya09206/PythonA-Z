def find_sum(arr:List[int]) -> int:

	sum_result = 0

	for i in range(len(arr)):
		sum_result += arr[i]  
	return sum_result


print(find_sum([2,3,43]))