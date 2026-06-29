def remove_duplicates(nums:List[int]) -> int:

	l = 0

	# loop thru list
	for r in range(nums):

		# check for duplicate
		if r != 0:
			# swap pointers
			nums[l], nums[r]