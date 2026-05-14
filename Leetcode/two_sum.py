def two_sum(nums:List[int], target:int) -> List[int]:

	seen = {}

	for i, num in enumerate(nums):

		complement = target - num 

		if complement in seen:
			return [seen[complement], i]
		else:
			seen[num] = i


nums = [2,7,11,15]
print(two_sum(nums, 9))

nums = [3,2,4]
print(two_sum(nums, 6))