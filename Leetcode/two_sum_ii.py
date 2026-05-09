def two_sum_ii(nums:List[int], target:int) -> int:

	l = 0
	r = len(nums) - 1

	while l < r:
		current_sum = nums[l] + nums[r]

		if current_sum == target:
			return nums[l + 1], nums[r + 1]
		elif current_sum < target:
			l += 1
		else:
			r -= 1

