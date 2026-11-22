def subarray_sum_equals_k(nums:List[int], k:int) -> int:

	# keep track of how many subarrays
	count = 0
	# running sum of values
	current_sum = 0
	# dictionary that contains frequency of prefixes
	prefix_count = {0: 1}

	# loop thru array
	for num in nums:
		# add num to current_sum
		current_sum += num
		# calculate the previous prefix sum needed
		needed_prefix = current_sum - k

		# check whether that needed prefix exists in the dictionary
		if needed_prefix in prefix_count:
			# if it exists, add its frequency to the answer
			count += prefix_count[needed_prefix]

		# Record the current running sum in the dictionary, increasing its frequency by one.
		prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

	# return count
	return count

	# for i in range(len(nums)):
	# 	running_sum = 0
	# 	for j in range(i, len(nums)):
	# 		running_sum += nums[j]
	# 		if running_sum == k:
	# 			count += 1

print(subarray_sum_equals_k([1,1,1], 2))
print(subarray_sum_equals_k([1,2,3], 3))
