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



        