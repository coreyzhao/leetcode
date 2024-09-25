class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        kbeauty = 0
    
        str_num = str(num)
        for r in range(k - 1, len(str_num)):
            l = r - k + 1
           
            if int(str_num[l:r + 1]) == 0:
                continue
            if num % int(str_num[l:r + 1]) == 0:
                kbeauty += 1

        return kbeauty