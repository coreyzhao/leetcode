class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        my_map = {}
        for i in words:
            my_map[i] = my_map.get(i, 0) + 1

        count = [] #[count, word]
        for key in my_map:
            count.append([-1 * my_map[key], key])

        heapq.heapify(count)

        res = []
        for i in range(k):
            ls = heapq.heappop(count)

            res.append(ls[1])

        return res

            
        