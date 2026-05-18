def contains_duplicate(nums:List[int]) -> bool:

	seen = {}

	for num in nums:

		if num in seen:
			return True
			
		seen[num] = num 

	return False

nums = [1,2,3,1]
nums2 = [1,2,3,4]
print(contains_duplicate(nums))
print(contains_duplicate(nums2))