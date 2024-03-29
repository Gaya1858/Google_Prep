import collections
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in squares[(r//3, c//3)]\
                        or board[r][c] in rows[r]\
                        or board[r][c] in cols[c]:
                    return False
                squares[(r // 3, c // 3)].add(board[r][c])
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])

        return  True
s =Solution()
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

# board = [["7",".",".",".","4",".",".",".","."],[".",".",".","8","6","5",".",".","."],[".","1",".","2",".",".",".",".","."],[".",".",".",".",".","9",".",".","."],[".",".",".",".","5",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".","2",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
# board = [[".",".",".",".","5",".",".","1","."],
#          [".","4",".","3",".",".",".",".","."],
#          [".",".",".",".",".","3",".",".","1"],
#          ["8",".",".",".",".",".",".","2","."],
#          [".",".","2",".","7",".",".",".","."],
#          [".","1","5",".",".",".",".",".","."],
#          [".",".",".",".",".","2",".",".","."],
#          [".","2",".","9",".",".",".",".","."],
#        [".",".","4",".",".",".",".",".","."]]
print(s.isValidSudoku(board))