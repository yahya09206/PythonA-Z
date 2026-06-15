def valid_sudoku(board:List[List[str]]) -> bool:

	# need to declare dicts
	rows = collections.defaultdict(set)
	cols = collections.defaultdict(set)
	cols = collections.defaultdict(set)

	