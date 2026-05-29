def top_k_frequent(nums: List[int], k: int) -> List[int]:

	count = {}

	for num in nums:

		count[num] = count.get(num, 0) + 1

	pairs_list = [(freq, num) for num, freq in count.items()]
	pairs_list.sort(reverse=True)

	return [num for freq, num in pairs_list[:k]]


print(top_k_frequent([1,1,1,2,2,3], 2))
print(top_k_frequent([1], 1))
print(top_k_frequent([1,2,1,2,1,2,3,1,3,2], 2))