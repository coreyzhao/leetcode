class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        visited = []

        def dfs(i):
            visited.append(i)

            for new_j in range(len(isConnected[i])):
                if isConnected[i][new_j] == 1 and new_j not in visited:

                    dfs(new_j)
            
            return

        
        count = 0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                count += 1

        return count
            