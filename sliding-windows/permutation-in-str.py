class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        hsh1 = Counter(s1)
        hsh2 = Counter(s2[:len_s1])

        if hsh1 == hsh2:
            return True


        for i in range(len_s1, len_s2):
            hsh2[s2[i]] += 1  
            hsh2[s2[i - len_s1]] -= 1  

           
            if hsh2[s2[i - len_s1]] == 0:
                del hsh2[s2[i - len_s1]]


            if hsh1 == hsh2:
                return True

        return False
    
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        my_map = {}
        l = 0
        target_map = {}
        for i in range(len(s1)):
            target_map[s1[i]] = target_map.get(s1[i], 0) + 1

        for r in range(len(s2)):
            my_map[s2[r]] = my_map.get(s2[r], 0) + 1

            if r - l + 1 > len(s1):
                my_map[s2[l]] -= 1
                if my_map[s2[l]] == 0:
                    del my_map[s2[l]]
                l += 1
                
            if my_map == target_map:
                return True

        return False

            


