def best_time(price:List[int]) -> int:

	# brute force
	# current_max = 0

	# for i in range(len(price)):
	# 	for j in range(i + 1, len(price)):
	# 		max_profit = price[j] - price[i]
	# 		if max_profit > current_max:
	# 			current_max = max_profit


	# return current_max


print(best_time([7,1,5,3,6,4]))
print(best_time([7,6,4,3,1]))