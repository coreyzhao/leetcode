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