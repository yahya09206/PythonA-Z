def two_sum_ii(nums:List[int], target:int) -> List:

	l = 0
	r = len(nums) - 1

	while l < r:

		current_sum = nums[l] + nums[r]

		if current_sum == target:
			return [l + 1, r + 1]
		elif current_sum < target:
			l += 1
		else: 
			r -= 1


num = [2,7,11,15]
num2 = [1,2,3,4,5]
print(two_sum_ii(num, 9))
print(two_sum_ii(num2, 5))