#inputs: lights = [[-3,2],[1,2],[3,3]]

class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        my_map = {}

        for ls in lights:
            start = ls[0] - ls[1]
            end = ls[0] + ls[1]
            my_map[start] = my_map.get(start, 0) + 1
            my_map[end + 1] = my_map.get(end + 1, 0) - 1
        
        
        sorted_map = sorted(my_map.items(), key=lambda x: x[0])

        res = 0
        count = 0
        my_max = 0
        for key, delta in sorted_map:
            count += delta
            if count > my_max:
                my_max = count
                res = key
        
        return res