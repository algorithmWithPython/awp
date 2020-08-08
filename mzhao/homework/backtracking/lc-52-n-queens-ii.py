import copy
import time
from typing import List
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

    def solveNQueens1(self, n: int) -> List[List[str]]:
        chess_board = [ ['.']*n for _ in range(n)]
        col = [False]*n
        ld = [False]*(2*n)
        rd= [False]*(2*n)
        res = 0
        def dfs(row):
            # base case
            nonlocal res
            if row == n:
                res+=1
                return

            for c in range(n):
                if not col[c] and not ld[row-c+n] and not rd[row+c]:
                    col[c], ld[row-c+n], rd[row+c] = True, True, True
                    chess_board[row][c] = 'Q'
                    dfs(row+1)
                    col[c], ld[row-c+n], rd[row+c] = False, False, False
                    chess_board[row][c] = '.' # backtracking
        dfs(0)
        return res



s = time.time()
n=12
print(Solution().solveNQueens(n))
e = time.time()
print(Solution().solveNQueens1(n))
print(f"seconds: {e-s}, {time.time()-e}")