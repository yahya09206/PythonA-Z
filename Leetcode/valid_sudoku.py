def valid_sudoku(board:List[List[str]]) -> bool:

	# need to declare dicts
	rows = collections.defaultdict(set)
	cols = collections.defaultdict(set)
	cols = collections.defaultdict(set)

	for r in range(9):
		for c in range(9):
			val = board[r][c]

			# skip if the value is an empty square
			if val == ".":
				continue