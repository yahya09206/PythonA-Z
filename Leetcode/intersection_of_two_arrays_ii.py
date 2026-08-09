def intersection_of_two_arrays(nums1:List[int], nums2:List[int]) -> List[int]:

	result = []
	nums2_copy = list(nums2)

	for num in nums1:
		if num in nums2_copy:
			result.append(num)
			nums2_copy.remove(

				num
			)

	return result


print(intersection_of_two_arrays([1,2,2,1], [2,2]))