def valid_sudoku(board:List[List[str]]) -> bool:

	# need to declare dicts
	rows = collections.defaultdict(set)
	cols = collections.defaultdict(set)
	boxes = collections.defaultdict(set)

	for r in range(9):
		for c in range(9):
			val = board[r][c]

			# skip if the value is an empty square
			if val == ".":
				continue

			# calculate the box tuple key using r // 3 and c // 3
			box_key = (r // 3, c // 3)

			if val in rows[r] or val in cols[c] or val in boxes[box_key]:
				return False
			else:
				rows[r].add(val)
				cols[c].add(val)
				boxes[box_key].add(val)

	return True