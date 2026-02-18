from typing import List

def move_zeroes(nums: List[int]) -> None:

	l = 0

	# loop through list
	for r in range(len(nums)):

		# check if index is equal to 0
		if nums[r]:

			temp = nums[l]
			nums[l] = nums[r]
			nums[r] = temp
			l += 1



nums = [0,1,0,3,12]
move_zeroes(nums)
print(nums)