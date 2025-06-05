class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        ins = 0

        while i < len(chars):

            group = 1

            while (group + i < len(chars) and chars[group + i] == chars[i]):
                group += 1

            chars[ins] = chars[i]
            ins += 1

            if group > 1:
                s = str(group)
                ls = list(s)

                

                chars[ins:ins+len(ls)] = ls

                ins += len(s)

            i += group

        return ins

            



            

