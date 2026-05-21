def two_sum(nums:List[int], target:int) -> List[int]:

	seen = {}

	for i, num in enumerate(nums):

		complement = target - num 

		if complement in seen:
			return [seen[complement], i]

		seen[num] = i 



nums = [2,7,11,15]
print(two_sum(nums, 26))