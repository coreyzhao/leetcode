class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        left = [0] * len(seats)
        right = [0] * len(seats)


        prev = float('-inf')
        for i in range(len(seats)):
            if seats[i] == 1:
                prev = i
            left[i] = i - prev

        nxt = float('inf')
        for i in range(len(seats) -1,-1,-1):
            if seats[i] == 1:
                nxt = i
            right[i] = nxt - i
        
        res = 0
        for i in range(len(seats)):
            curdist = min(left[i], right[i])
            res = max(res, curdist)

        return res