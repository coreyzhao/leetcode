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
            