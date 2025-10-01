class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set() #[x,y]
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(x, y):
            visited.add((x,y))

            for ls in dirs:
                next_x = x + ls[0]
                next_y = y + ls[1]
                if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]) or (next_x, next_y) in visited:
                    continue

                if grid[next_x][next_y] != "1":
                    continue

                dfs(next_x, next_y)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    count += 1

        return count


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        visited = set()
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(r,c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or (r,c) in visited:
                return

            if grid[r][c] == "0":
                return

            visited.add((r,c))
            for ls in dirs:
                new_r = r + ls[0]
                new_c = c + ls[1]

                dfs(new_r,new_c)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    dfs(r,c)
                    count += 1

        return count
            
            
            
        