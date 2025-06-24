class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        res = []

        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)

        return res
    


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtracking(ls):
            if len(ls) == 0:
                return [[]]

            ls_perms = backtracking(ls[1:])
            final = []
            for new_ls in ls_perms:
                for i in range(len(new_ls) + 1):
                    res = new_ls.copy()
                    res.insert(i, ls[0])
                    final.append(res)

            return final



        return backtracking(nums)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        def dfs(ls):

            if ls == []:
                return [[]]

            num = ls[0]
            new_ls = ls[1:]

            
            perms = dfs(new_ls)
            res = []
            for i in range(len(new_ls) + 1):
                for ls in perms:
                    ls_copy = ls.copy()
                    ls_copy.insert(i, num)
                    res.append(ls_copy)
            return res

        return dfs(nums)