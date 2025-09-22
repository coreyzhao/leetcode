class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        if len(mat) * len(mat[0]) != r * c:
            return mat

        cur_r = 0
        cur_c = 0
        flattened_ls = []
        
        for i in range(rows):
            for j in range(cols):
                flattened_ls.append(mat[i][j])

        res = []
        new_row = []
        print(flattened_ls)
        for i in flattened_ls: 
            if cur_c == c:
                res.append(new_row)
                new_row = []
                cur_r += 1
                cur_c = 0
                
            cur_c += 1
            new_row.append(i)

        res.append(new_row)
        return res