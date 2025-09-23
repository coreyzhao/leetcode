class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        item = ""
        for i in range(1,len(path)):
            
            if (path[i] != "/"):
                item += path[i]
            else:
                if item == "":
                    item = ""

                    continue
                elif item == ".":
                    item = ""

                    continue
                elif item == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(item)
                item = ""

        res = ""
        if item:
            if item == "":
                    item = ""
            elif item == ".":
                item = ""
            elif item == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(item)

        for i in stack:
            res += "/"
            res += i

        if stack == []:
            return "/"

        return res


            

