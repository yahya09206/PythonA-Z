def remove_duplicates_from_sorted(nums:List[int]) -> int:

	result = []

	for i in nums:
		if i not in result:
			result.append(i)

	return result


print(remove_duplicates_from_sorted([1,1,2]))
print(remove_duplicates_from_sorted([0,0,1,1,1,2,2,3,3,4]))