import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        chess_board = [ ['.']*n for _ in range(n)]
        res = 0
        def dfs(row):
            # base case
            nonlocal res
            if row == n:
                res+=1
                return

            for c in range(n):
                good_spot =True
                for pre_row in range(row):
                    c1 = c - (row-pre_row)
                    c2 = c + (row-pre_row)
                    if chess_board[pre_row][c] == 'Q' or \
                       (c1>=0 and chess_board[pre_row][c1] == 'Q') or \
                       (c2<n and chess_board[pre_row][c2] == 'Q'):
                        good_spot = False
                        break
                if good_spot:
                    chess_board[row][c] = 'Q'
                    dfs(row+1)
                    chess_board[row][c] = '.' # backtracking
        dfs(0)
        return res