class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [] # [dist, x, y]
        for ls in points:
            dist = ls[0] ** 2 + ls[1] ** 2
            min_heap.append([dist, ls[0], ls[1]])

        heapq.heapify(min_heap)
        res = []

        while k > 0:
            cur_ls = heapq.heappop(min_heap)
            res.append([cur_ls[1], cur_ls[2]])
            k -= 1

        return res
