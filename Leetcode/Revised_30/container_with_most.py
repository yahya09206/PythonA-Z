def container_with_most(height:List[int]) -> int:

	ans = 0

	l = 0
	r = len(height) - 1

	while l < r:

		area = min(height[l], height[r]) * (r - l)
		ans = max(area, ans)

		if height[l] < height[r]:
			l += 1
		else:
			r -= 1

	return ans



nums = [1,8,6,2,5,4,8,3,7]
print(container_with_most(nums))