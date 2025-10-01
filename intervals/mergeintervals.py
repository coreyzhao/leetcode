class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda ls : ls[0])
        prev = intervals[0]
        res = []
        for i in range(1, len(intervals)):

            if intervals[i][0] <= prev[1]:
                prev[1] = max(intervals[i][1], prev[1])
            else:
                res.append(prev)
                prev = intervals[i]

        res.append(prev)

        return res
