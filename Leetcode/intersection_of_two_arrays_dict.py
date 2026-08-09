def intersection_of_two_arrays(nums1:List[int], nums2:List[int]) -> List[int]:

	set1 = set(nums1)
	result_set = set()

	for num in nums2:
		if num in set1:
			result_set.add(num)

	return list(result_set)
	# result = []

	# for i in nums1:
	# 	for j in nums2:
	# 		if i == j and i not in result:
	# 			result.append(i)

	# return result


print(intersection_of_two_arrays([1,2,2,1], [2,2]))
print(intersection_of_two_arrays([4,9,5], [9,4,9,8,4]))