def intersection_of_two_arrays(nums1:List[int], nums2:List[int]) -> List[int]:

	count_map = {}
	result = []

	for num in nums1:
		count_map[num] = count_map.get(num, 0) + 1

	for num in nums2:
		if num in count_map and count_map[num] > 0:
			result.append(num)
			count_map[num] -= 1

	return result


	# result = []
	# nums2_copy = list(nums2)

	# for num in nums1:
	# 	if num in nums2_copy:
	# 		result.append(num)
	# 		nums2_copy.remove(

	# 			num
	# 		)

	# return result


print(intersection_of_two_arrays([1,2,2,1], [2,2]))
print(intersection_of_two_arrays([4,9,5], [9,4,9,8,4]))