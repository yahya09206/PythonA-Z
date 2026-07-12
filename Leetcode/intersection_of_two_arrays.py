def intersection_of_two_arrays(nums1:List[int], nums2:List[int]) -> List[int]:

	l = 0
	r = 0
	nums1.sort()
	nums2.sort()
	result = []

	while l < len(nums1) and r < len(nums2):

		if nums1[l] == nums2[r] and nums1[l] not in result:
			result.append(nums1[l])
			l += 1
			r += 1
		elif nums1[l] < nums2[r]:
			l += 1
		else:
			r += 1

	return result
	# res = list()

	# for i in nums1:
	# 	for j in nums2:
	# 		if i == j and i not in res:
	# 			res.append(i)

	# return res


print(intersection_of_two_arrays([1,2,2,1], [2,2]))
print(intersection_of_two_arrays([4,9,5], [9,4,9,8,4]))