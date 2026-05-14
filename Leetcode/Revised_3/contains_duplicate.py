def contains_dupe(nums:List[int]) -> bool:

	seen = set()

	for num in nums:

		if num in seen:
			return True
		else:
			seen.add(num)

	return False



numbers = [1,2,3]
print(contains_dupe(numbers))