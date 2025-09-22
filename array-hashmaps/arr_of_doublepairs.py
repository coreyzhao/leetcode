class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        my_map = {}

        for i in arr:
            my_map[i] = my_map.get(i, 0) + 1

        sorted_arr = sorted(arr, key=abs)

        for i in range(len(sorted_arr)):
            dbl = sorted_arr[i] * 2

            if my_map[sorted_arr[i]] < 1:
                continue

            if dbl in my_map and my_map[dbl] >= 1 and my_map[sorted_arr[i]] >= 1:
                my_map[dbl] -= 1
                my_map[sorted_arr[i]] -= 1
            else:
                return False

        return True


        
        