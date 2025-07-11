class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rLS = list(ransomNote)
        magLS = list(magazine)

        print(rLS)
        for i in rLS:

            if i in magLS:
                magLS.remove(i)
            else:
                return False

        return True        