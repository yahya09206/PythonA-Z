def majority_element(nums:List[int]) -> int:

	count = {}

	for num in nums:
		count[num] = count.get(num, 0) + 1
		if count[num] > len(nums) // 2:
			return num

	# Brute force TLE
	# for num in nums:
	# 	count = 0
	# 	for element in nums:
	# 		if element == num:
	# 			count += 1
	# 	if count > len(nums) // 2:
	# 		return num


print(majority_element([3,2,3]))
print(majority_element([2,2,1,1,1,2,2]))