def replace_elements(arr:List[int]) -> List[int]:

	max_so_far = -1

	for i in range(len(arr) - 1, -1, -1):
		temp = arr[i]
		arr[i] = max_so_far
		max_so_far = max(max_so_far, temp)

	return arr

	# result = [0] * len(arr)

	# for i in range(len(arr) - 1):
	# 	current_max = arr[i + 1]
	# 	for j in range(i + 1, len(arr)):
	# 		if current_max < arr[j]:
	# 			current_max = arr[j]

	# 	result[i] = current_max
	# result[len(arr) - 1] = -1


	# return result

print(replace_elements([17,18,5,4,6,1]))