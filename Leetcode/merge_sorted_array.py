def merge_sorted_array(nums1:List[int], m:int, nums2:List[int], n:int) -> None:

	pointer1 = m - 1
	pointer2 = len(nums2) - 1
	write_index = (m + n) - 1

	while pointer1 >= 0 and pointer2 >= 0:

		if nums1[pointer1] > nums2[pointer2]:
			nums1[write_index] = nums1[pointer1]
			pointer1 -= 1
			write_index -= 1
		else:
			nums1[write_index] = nums2[pointer2]
			pointer2 -= 1
			write_index -= 1

	while pointer2 >= 0:
			nums1[write_index] = nums2[pointer2]
			pointer2 -= 1
			write_index -= 1
