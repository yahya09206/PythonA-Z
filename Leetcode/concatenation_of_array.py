def concatenation_of_array(nums:List[int]) -> List[int]:

	result = [0] * (2 * len(nums))

	for i in range(len(nums)):
		result[i] = nums[i]
		result[i + len(nums)] = nums[i]

	return result

	# return nums * 2


print(concatenation_of_array([1,2,1]))
print(concatenation_of_array([1,3,2,1]))

