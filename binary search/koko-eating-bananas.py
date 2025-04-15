class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = max(piles) 
        h_required = 0

        while(min_speed <= max_speed):
            cur_speed = (max_speed + min_speed) // 2
            h_required = 0

            for num_bananas in piles:
                hours_needed = num_bananas/cur_speed
                if int(hours_needed) == hours_needed:
                    h_required += int(hours_needed)
                else:
                    h_required += (int(hours_needed) + 1)


            if h_required > h:
                min_speed = cur_speed + 1
            else:
                max_speed = cur_speed - 1


        return min_speed