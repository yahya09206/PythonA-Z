def replace_elements(arr:List[int]) -> List[int]:

	result = [0] * len(arr)

	for i in range(len(arr) - 1):
		current_max = arr[i + 1]
		for j in range(i + 1, len(arr)):
			if current_max < arr[j]:
				current_max = arr[j]

		result[i] = current_max
	result[len(arr) - 1] = -1


	return result

print(replace_elements([17,18,5,4,6,1]))