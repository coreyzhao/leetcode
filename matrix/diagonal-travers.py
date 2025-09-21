class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        res = []

        cur_row = 0
        cur_col = 0
        goingup = True
        while (len(res) < len(mat) * len(mat[0])):

            if goingup:
                while cur_row >= 0 and cur_col < cols:
                    res.append(mat[cur_row][cur_col])
                    cur_row -= 1
                    cur_col += 1
                
                if cur_row < 0 and cur_col >= cols:
                    cur_row += 2
                    cur_col -= 1
                elif cur_row < rows and cur_col >= cols:
                    cur_row += 2
                    cur_col -= 1
                else:
                    cur_row += 1

                goingup = False
            else:
                while cur_row < rows and cur_col >= 0:
                    res.append(mat[cur_row][cur_col])
                    cur_row += 1
                    cur_col -= 1

                if 0 <= cur_row < rows and cur_col < 0:
                    cur_col += 1
                # elif cur_row >= rows and 0 <= cur_col < cols:
                #     cur_col += 2
                #     cur_row -= 1
                else:
                    cur_col += 2
                    cur_row -= 1
                goingup = True

        return res