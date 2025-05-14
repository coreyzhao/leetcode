class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(c,r,i):
            if i == len(word):
                return True

            if c < 0 or r < 0 or r >= ROWS or c >= COLS or (r,c) in visited or word[i] != board[r][c]:
                return False

            visited.add((r,c))
            res = (dfs(c + 1, r, i + 1) or
                        dfs(c - 1, r, i + 1) or
                        dfs(c, r + 1, i + 1) or
                        dfs(c, r - 1, i + 1))
            visited.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(c,r,0):
                    return True


        return False
    
#2


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = []
        def dfs(i,j,index):
            

            if index == len(word):
                return True

            if (i < 0
            or i >= len(board)
            or j < 0
            or j >= len(board[0])
            or [i,j] in visited):
                return False

            if board[i][j] != word[index]:
                return False

            visited.append([i,j])

            found =  (dfs(i + 1, j, index + 1) 
            or dfs(i - 1, j, index + 1) 
            or dfs(i, j + 1, index + 1) or dfs(i, j - 1, index + 1))
            visited.remove([i,j])

            return found


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = []
                    if (dfs(i,j,0)):
                        return True



        return False



            


            