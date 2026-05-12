def contains_nearby_duplicate(nums:List[int], k:int) -> bool:

	seen = {} # keep track of already seen numbers

	for i, num in enumerate(nums):

		if num in seen:
			if abs(i - seen[num]) <= k:
				return True

		seen[num] = i 

	return False