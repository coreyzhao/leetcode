class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix) - 1

        while l < r:
            for i in range(r - l):

                top = l
                bot = r

                topLeft = matrix[top][l + i]

                # move bottom left to top left
                print(top, l+i, bot - i, l)
                matrix[top][l + i] = matrix[bot - i][l]

                # move bottom right to bottom left
                matrix[bot - i][l] = matrix[bot][r - i]

                # move top right to bottom right
                matrix[bot][r - i] = matrix[top + i][r]

                # move top left to top right
                matrix[top + i][r] = topLeft

            l += 1
            r -= 1

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        w = 0
        h = len(matrix) - 1
        while w < h:

            for j in range(h - w):
                
                temp = matrix[w][w + j]

                matrix[w][w + j] = matrix[h - j][w]

                matrix[h - j][w] = matrix[h][h - j]

                matrix[h][h - j] = matrix[w + j][h]

                matrix[w + j][h] = temp
            
            w += 1
            h -= 1


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix[0]) - 1

        t = 0
        b = len(matrix) - 1

        while (l < r):
            for i in range(r - l):

                temp = matrix[t][l + i]

                
                matrix[t][l + i] = matrix[b - i][l]

                matrix[b - i][l] = matrix[b][r - i]

                matrix[b][r - i] = matrix[t + i][r]

                matrix[t + i][r] = temp

            l += 1
            t += 1
            r -= 1
            b -= 1

        
        










        