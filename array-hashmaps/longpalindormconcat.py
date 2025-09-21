class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        same_letters = {}
        diff_letters = {}
        count = 0

        for i in words:
            if i[0] == i[1]:
                if i in same_letters:
                    same_letters[i] += 1
                else:
                    same_letters[i] = 1
                count += 2

            else:
                if i[::-1] in diff_letters and diff_letters[i[::-1]] > 0:
                    diff_letters[i[::-1]] -= 1
                    count += 4
                else:
                    diff_letters[i] = diff_letters.get(i, 0) + 1
        one_odd = 0
        for key in same_letters:
            
            if same_letters[key] % 2 != 0:
                if one_odd == 0:
                    one_odd += 1
                    continue
                else:
                    count -= 2

            

        return count
                
