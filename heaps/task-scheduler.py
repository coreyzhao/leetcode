class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = {}
        

        for i in tasks:
            if i in counts:
                counts[i] += 1

            else:
                counts[i] = 1

        max_heap = []

        for i in counts.values():
            max_heap.append(-1 * i)


        heapq.heapify(max_heap)
        time = 0
        q = [] # [count, time_to_be_released]
        while max_heap or q:

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q[0][0])
                q.pop(0)

            if max_heap:

                

                cur = heapq.heappop(max_heap)

                if cur != -1:
                    q.append([cur + 1, time + n + 1])

            time += 1

        return time

            




