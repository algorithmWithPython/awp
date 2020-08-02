def queens(numberOfQueens):
    chess_board = [ ['-']*numberOfQueens for _ in range(numberOfQueens)]
    def dfs(row):
        # base case
        if row == numberOfQueens:
            print_chess_table()
            return
            
        for c in range(numberOfQueens):
            good_spot =True
            for pre_row in range(row):
                c1 = c - (row-pre_row)
                c2 = c + (row-pre_row)
                if chess_board[pre_row][c] == 'Q' or \
                   (c1>=0 and chess_board[pre_row][c1] == 'Q') or \
                   (c2<numberOfQueens and chess_board[pre_row][c2] == 'Q'):
                    good_spot = False
                    break
            if good_spot:
                chess_board[row][c] = 'Q'
                dfs(row+1)
                chess_board[row][c] = '-' # backtracking

    def print_chess_table():
        for i in range(numberOfQueens):
            print(' '.join(chess_board[i]))
        print()

    # for i in range(numberOfQueens):
    #     chess_board[0][i] = 'Q'
    #     dfs(1)
    #     chess_board[0][i] = '-' # backtracking
    
    dfs(0)

queens(4)
