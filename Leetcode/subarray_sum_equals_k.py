def subarray_sum_equals_k(nums:List[int], k:int) -> int:

	count = 0
	current_sum = 0
	prefix_count = {0: 1}

	for num in nums:
		current_sum += num
		needed_prefix = current_sum - k 

		if needed_prefix in prefix_count:
			count += prefix_count[needed_prefix]

		prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

	# for i in range(len(nums)):
	# 	running_sum = 0
	# 	for j in range(i, len(nums)):
	# 		running_sum += nums[j]
	# 		if running_sum == k:
	# 			count += 1

	return count

print(subarray_sum_equals_k([1,1,1], 2))
print(subarray_sum_equals_k([1,2,3], 3))
