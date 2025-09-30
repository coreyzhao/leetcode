class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        
        visited = set()
        def dfs(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return

            if board[r][c] != "O":
                return

            board[r][c] = "T"
            for ls in dirs:
                new_r = r + ls[0]
                new_c = c + ls[1]

                dfs(new_r, new_c)

        for c in range(COLS):
            dfs(0,c)
            dfs(ROWS - 1, c)

        for r in range(1, ROWS - 1):
            dfs(r,0)
            dfs(r,COLS - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O" 
            
            

            