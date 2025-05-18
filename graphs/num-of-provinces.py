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
            


# 2

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = []
        count = 0

        def dfs(i):
            cur_ls = isConnected[i]
            visited.append(i)

            for j in range(len(cur_ls)):
                if cur_ls[j] == 1 and j not in visited:
                    dfs(j)

            return
        
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                count += 1


        return count
