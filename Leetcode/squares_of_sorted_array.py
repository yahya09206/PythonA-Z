def squares_of_sorted_array(nums:List[int]) -> List[int]:

	l = 0
	r = len(nums) - 1
	res = [0] * len(nums)
	p = len(res) - 1


	while l <= r:

		left_square = nums[l] * nums[l]
		right_square = nums[r] * nums[r]

		if left_square < right_square:
			res[p] = right_square
			r -= 1
		else:
			res[p] = left_square
			l += 1
			
		p -= 1

	return res

	# res = []

	# for num in nums:

	# 	res.append(num**2)

	# res.sort()
	
	# return res
	


print(squares_of_sorted_array([-4,-1,0,3,10]))


