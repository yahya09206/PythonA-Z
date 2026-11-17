def best_time_ii(prices:List[int]) -> int:

	# brute force/optimal

	# keep track of a running total
	total_profit = 0

	for i in range(1, len(prices)):

		if prices[i] - prices[i - 1] > 0:
			total_profit += prices[i] - prices[i - 1]

	return total_profit

print(best_time_ii([7,1,5,3,6,4]))

