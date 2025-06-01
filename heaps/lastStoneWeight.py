class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)


        while len(stones) > 1:
            max1 = heapq._heappop_max(stones)
            max2 = heapq._heappop_max(stones)

            if max1 < max2:
                heapq.heappush(stones, max2 - max1)
            else:
                heapq.heappush(stones, max1 - max2)

            heapq._heapify_max(stones)

        if len(stones) == 0:
            return 0

        return heapq._heappop_max(stones)

#


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i] * -1

        heapq.heapify(stones)

        while (len(stones) > 1):
            largest = -heapq.heappop(stones)
            next_largest = -heapq.heappop(stones)

            new_stone = largest - next_largest
            if (new_stone):
                heapq.heappush(stones, -1 * new_stone)

        if len(stones) == 1:
            return stones[0] *-1

        return 0


        