def intersection_of_two_arrays(nums1:List[int], nums2:List[int]) -> List[int]:

	res = list()

	for i in nums1:
		for j in nums2:
			if i == j and i not in res:
				res.append(i)

	return res


print(intersection_of_two_arrays([1,2,2,1], [2,2]))
print(intersection_of_two_arrays([4,9,5], [9,4,9,8,4]))