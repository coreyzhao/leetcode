class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        my_map = {}
        for i in range(numCourses):
            my_map[i] = []

        for ls in prerequisites:
            my_map[ls[1]].append(ls[0])

        visited = set()
        def dfs(crs):
            if crs in visited:
                return False

            if my_map[crs] == []:
                return True

            visited.add(crs)
            for new_crs in my_map[crs]:
                if not (dfs(new_crs)):
                    return False

            visited.remove(crs)

            my_map[crs] = []
            return True

        for crs in range(numCourses):
            if dfs(crs):
                continue
            else:
                return False

        return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        my_map = {}
        for i in range(numCourses):
            my_map[i] = []

        for ls in prerequisites:
            my_map[ls[1]].append(ls[0])

        print(my_map)
        visit = set()
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if my_map[crs] == []:
                return True

            visited.add(crs)
            visit.add(crs)
            for new_crs in my_map[crs]:
                if not dfs(new_crs):
                    return False

            visited.remove(crs)
            my_map[crs] = []
            return True

        
        for i in range(numCourses):
            if i not in visit:
                if not dfs(i):
                    return False

        return True