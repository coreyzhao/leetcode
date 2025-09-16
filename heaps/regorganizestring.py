class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {} #char : count
        for i in s:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1

        max_heap = []
        for i in count:
            max_heap.append([-1 * count[i], i])

        heapq.heapify(max_heap)
        res = ""
        prev = None
        while max_heap or prev:
            if prev and not max_heap:
                return ""
            
            count, char = heapq.heappop(max_heap)
            res += char
            count += 1

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None

            if count != 0:
                prev = [count, char]

        return res

