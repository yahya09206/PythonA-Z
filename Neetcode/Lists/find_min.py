def find_min(arr:List[int]) -> int:

	min = arr[0];

	for i in arr: 
		if i < min:
			min = i 
	return min


print(find_min([2,3,43,65,78,4,110,999,1,20,4300]))
print(find_min([2,3,43,65,7800,4,110,999,20]))