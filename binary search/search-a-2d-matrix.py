class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r1 = len(matrix) - 1
        r2 = len(matrix[0]) - 1

        l1 = 0
        l2 = 0

        while l1 <= r1:
            mid1 = l1 + ((r1 - l1) // 2)

            
            if matrix[mid1][0] <= target and target <= matrix[mid1][r2]:
                l1 = 99999999
            elif matrix[mid1][0] > target:
                r1 = mid1 - 1
            elif matrix[mid1][r2] < target:
                l1 = mid1 + 1

        while l2 <= r2:
            mid2 = l2 + ((r2 - l2) // 2)
            if matrix[mid1][mid2] == target:
                return True

            if matrix[mid1][mid2] < target:
                l2 = mid2 + 1
            elif matrix[mid1][mid2] > target:
                r2 = mid2 - 1

        return False
