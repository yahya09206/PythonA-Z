def find_max(arr:List[int]) -> int:

	max = arr[0]

	for i in arr:
		if i > max:
			max = i
	return max


print(find_max([2,3,43,65,78,4,110,999,20,4300]))
print(find_max([2,3,43,65,7800,4,110,999,20]))

