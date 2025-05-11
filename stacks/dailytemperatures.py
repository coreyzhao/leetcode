class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #[temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                curTemp, curIndex = stack.pop()
                res[curIndex] = i - curIndex

            stack.append([t,i])

        return res
    

#2

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)

        stack = []

        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                info_ls = stack.pop()
                res[info_ls[1]] = i - info_ls[1]
            
            stack.append([temp, i])

        return res

#3

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = [] # [temp, i]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                new_res = stack.pop()
                res[new_res[1]] = (i - new_res[1])

            stack.append([temp, i])


        return res
