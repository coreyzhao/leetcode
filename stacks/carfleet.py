class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        merged_ls = []
        for i in range(len(position) -1,-1,-1):
            merged_ls.append([position[i], speed[i]])

        merged_ls.sort(key=lambda ls : ls[0])

        print(merged_ls)
        
        stack = []
        for i in range(len(position) -1,-1,-1):
            arrivaltime = (target - merged_ls[i][0]) / merged_ls[i][1]

            if stack and stack[-1] >= arrivaltime:
                continue
            else:
                stack.append(arrivaltime)

        return len(stack)
