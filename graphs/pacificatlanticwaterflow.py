class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        def dfs(r, c, prevHeight, visited):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            
            if (r,c) in visited:
                return

            if heights[r][c] < prevHeight:
                return

            visited.add((r,c))
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]
            for ls in dirs:
                new_row = r + ls[0]
                new_col = c + ls[1]

                dfs(new_row, new_col, heights[r][c], visited)

        pac = set()
        atl = set()
        for c in range(cols):
            
            dfs(0,c,0,pac)
            dfs(rows - 1,c,0,atl)

        for r in range(1, rows):
            dfs(r,0,0,pac)
            dfs(r - 1,cols - 1,0,atl)
            

        print(pac, atl)
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res
        
