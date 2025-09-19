class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda ls: ls[0])
        res = []
        prev = intervals[0]

        if len(intervals) == 1:
            return intervals

        for i in range(1, len(intervals)):
            if intervals[i][0] <= prev[1]:
                prev = [prev[0], max(prev[1], intervals[i][1])]

            else:
                res.append(prev)
                prev = intervals[i]

        res.append(prev)

        return res

