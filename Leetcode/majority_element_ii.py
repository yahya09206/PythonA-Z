def majority_element_ii(nums:List[int]) -> List[int]:

	result = []


	for i in range(len(nums)):
		counter = 0
		for j in range(len(nums)):
			if nums[i] == nums[j]:
				counter += 1

		if counter > len(nums) // 3: 
			if nums[i] not in result:
				result.append(nums[i])
			
		counter = 0

	return result

print(majority_element_ii([3,2,3]))
print(majority_element_ii([1]))
print(majority_element_ii([1,2]))


