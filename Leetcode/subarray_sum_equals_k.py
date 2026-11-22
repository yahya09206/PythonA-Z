def subarray_sum_equals_k(nums:List[int], k:int) -> int:

	count = 0

	for i in range(len(nums)):
		running_sum = 0
		for j in range(i, len(nums)):
			running_sum += nums[j]
			if running_sum == k:
				count += 1

	return count

print(subarray_sum_equals_k([1,1,1], 2))
