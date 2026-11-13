def sort_colors(nums:List[int]) -> List[int]:

	for i in range(len(nums)):
		for j in range(i, len(nums)):
			if nums[i] > nums[j]:
				temp = nums[i]
				nums[i] = nums[j]
				nums[j] = temp

	return nums

print(sort_colors([2,0,2,1,1,0]))

