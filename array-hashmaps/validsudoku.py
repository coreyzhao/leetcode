class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r_map = {}
        c_map = {}
        sub_map = {}
        for i in range(len(board)):
            r_map[i] = []
            c_map[i] = []
        
        for r in range(3):
            for c in range(3):
                sub_map[(r,c)] = []
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]

                if val == ".":
                    continue

                sub_i = ((r // 3), (c // 3))
                if val in r_map[r] or val in c_map[c] or val in sub_map[sub_i]:
                    print(r,c)
                    return False
                
                r_map[r].append(val)
                c_map[c].append(val)
                sub_map[sub_i].append(val)


        return True