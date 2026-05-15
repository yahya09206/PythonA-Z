def contains_dupe(list:List[int], k: int) -> bool:

	seen = {}

	for i, num in enumerate(list):

		if num in seen:
			if i - seen[num] <= k:
				return True
		
		seen[num] = i 
	return False



nums = [1,2,3,1]
nums2 = [1,0,1,1]
nums3 = [1,2,3,1,2,3]
print(contains_dupe(nums, 3))
print(contains_dupe(nums2, 1))
print(contains_dupe(nums3, 2))