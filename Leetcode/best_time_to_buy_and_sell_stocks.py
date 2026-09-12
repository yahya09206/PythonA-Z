def best_time(price:List[int]) -> int:

	min_price = price[0]
	max_profit = 0

	for i in range(len(price)):
		if min_price > price[i]:
			min_price = price[i]

		current_max = price[i] - min_price

		if current_max > max_profit:
			max_profit = current_max

	return max_profit



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