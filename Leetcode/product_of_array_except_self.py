def product_of_array_except_self(nums: List[int]) -> List[int]:

	prefix = [1] * len(nums)
	suffix = [1] * len(nums)

	for i in range(1, len(nums)):
		prefix[i] = nums[i - 1] * prefix[i - 1]
	
	for j in range(len(nums) - 2, -1, -1):
		suffix[j] = nums[j + 1] * suffix[j + 1]

	result = []

	for i in range(0, len(nums)):
		result.append(prefix[i] * suffix[i])

	return result


print(product_of_array_except_self([1,2,3,4]))
print(product_of_array_except_self([-1,1,0,-3,3]))