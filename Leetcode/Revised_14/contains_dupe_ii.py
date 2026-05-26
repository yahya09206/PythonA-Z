def contains_dupe_ii(nums:List[int], k:int) -> bool:

	seen = {}

	for i, num in enumerate(nums):

		if num in seen:

			if i - seen[num] <= k:
				return True

		seen[num] = i 

	return False

print(contains_dupe_ii([1,2,3,1,2,3],2))
print(contains_dupe_ii([1,0,1,1],1))