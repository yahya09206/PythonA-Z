def sort_colors(nums:List[int]) -> None:

	count_map = {}

	for num in nums:
		count_map[num] = count_map.get(num, 0) + 1


	idx = 0

	for i in range(3):
		for _ in range(count_map.get(i, 0)):
			nums[idx] = i
			idx += 1

	return nums


nums = [2, 0, 2, 1, 1, 0]

sort_colors(nums)

print(nums)


	# for i in range(len(nums)):
	# 	for j in range(i, len(nums)):
	# 		if nums[i] > nums[j]:
	# 			temp = nums[i]
	# 			nums[i] = nums[j]
	# 			nums[j] = temp

#print(sort_colors([2,0,2,1,1,0]))

