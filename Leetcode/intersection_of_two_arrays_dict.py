def intersection_of_two_arrays(nums1:List[int], nums2:List[int]):

	result = []

	for i in nums1:
		for j in nums2:
			if i == j and i not in result:
				result.append(i)

	return result


print(intersection_of_two_arrays([1,2,2,1], [2,2]))
print(intersection_of_two_arrays([4,9,5], [9,4,9,8,4]))