import collections  # <--- Add this exact line at the top!
from typing import List

def valid_sudoku(board:List[List[str]]) -> bool:

	# need to declare dicts
	rows = collections.defaultdict(set)
	cols = collections.defaultdict(set)
	boxes = collections.defaultdict(set)

	# loop through board
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



print(valid_sudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print(valid_sudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))