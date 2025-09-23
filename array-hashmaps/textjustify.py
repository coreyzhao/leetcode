class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        i = 0
        line = []
        length = 0
        res = []

        while i < len(words):
            if length + len(line) + len(words[i]) > maxWidth:
                
                extra_chars = maxWidth - length
                spaces_between_each = extra_chars // (max( len(line) - 1, 1))
                remainder = extra_chars % (max ( len(line) - 1, 1))

                for j in range(max(len(line) -1, 1)):
                    line[j] += " " * spaces_between_each
                    if remainder:
                        line[j] += " "
                        remainder -= 1
                
                res.append("".join(line))
                line = []
                length = 0

            line.append(words[i])
            length += len(words[i])
            i += 1

        final_line = " ".join(line)
        extra_spaces = maxWidth - len(final_line)
        final_line += " " * extra_spaces

        res.append(final_line)

        return res
    
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        line = []
        length = 0
        res = []

        for i in words:
            
            if length + len(i) + len(line) > maxWidth:

                chars_left = maxWidth - length
                chars_space = chars_left // max(len(line) - 1, 1)
                remainder = chars_left % max(len(line) - 1, 1)

                for j in range(max(len(line) -1, 1)):
                    line[j] += " " * chars_space

                if remainder:
                    for j in range(remainder):
                        line[j] += " "

                res.append("".join(line))

                line = []
                length = 0
                    

            line.append(i)
            length += len(i)

        last = " ".join(line)
        last += " " * (maxWidth - len(last))
        res.append(last)

        return res
