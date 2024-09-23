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


