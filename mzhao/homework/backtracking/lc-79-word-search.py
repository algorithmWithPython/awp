class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rl = len(board)
        cl = len(board[0])
        wl = len(word)
        p = []

        dr = [(1,0), (0, 1), (-1, 0), (0, -1)]

        def dfs(i,j,wp):
            if board[i][j] != word[wp]:
                return False
            
            if wp == wl-1:
                return True
            
            tmp = board[i][j]
            board[i][j]='0'
            res = False
            for d in dr:
                if 0<=i+d[0]<rl and \
                   0<=j+d[1]<cl:
                    res = res or dfs(i+d[0], j+d[1], wp+1)
            board[i][j]=tmp
            return res
        #get all start point
        res = False
        for i in range(rl):
            for j in range(cl):
                res = res or dfs(i, j, 0) 
        return res