def concatenation_of_array(nums:List[int]) -> List[int]:

	n = len(nums)
	ans = [0] * (2 * n)

	for i in range(n):

		ans[i] = nums[i]
		ans[i + n] = nums[i]

	return ans

