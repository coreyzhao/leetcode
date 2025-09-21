class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # r1 + r2 must be equal to 60 or 0
        my_map = {} # remainder : count

        for i in time:
            remainder = i % 60
            if remainder in my_map:
                my_map[remainder] += 1
            else:
                my_map[remainder] = 1

        count = 0
        for key in my_map:
            
            if 0 < key < 30:
                desired_remainder = 60 - key
                if desired_remainder in my_map:
                    count += my_map[desired_remainder] * my_map[key]

            elif key == 0 or key == 30:
                count += (my_map[key] - 1) * my_map[key] // 2

            
        return count

        
            


                            
                