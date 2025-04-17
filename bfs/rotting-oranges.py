class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        fresh = 0
        q = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i, j])
    
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while len(q) > 0 and fresh > 0:

            for i in range(len(q)):

                coords = q.pop(0)
                for ls in directions:
                    new_coords = [0,0]
                    new_coords[0] = coords[0] + ls[0]
                    new_coords[1] = coords[1] + ls[1]

                    if (new_coords[0] > len(grid) - 1 or 
                    new_coords[1] > len(grid[0]) - 1 or 
                    new_coords[0] < 0 or 
                    new_coords[1] < 0):
                        continue

                    if grid[new_coords[0]][new_coords[1]] != 1:
                        continue
                    
                    grid[new_coords[0]][new_coords[1]] = 2
                    fresh -= 1
                    q.append(new_coords)

            count += 1

        if fresh > 0:
            return -1
        else:
            return count