class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        from typing import List

        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0
        bottom = ROWS - 1

        # Binary search to find the correct row
        while top <= bottom:
            row = (top + bottom) // 2

            if target > matrix[row][COLS - 1]:
                top = row + 1

            elif target < matrix[row][0]:
                bottom = row - 1

            else:
                break

        # Target cannot be in any row
        if not (top <= bottom):
            return False

        row = (top + bottom) // 2

        # Binary search inside the row
        left = 0
        right = COLS - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True

            elif matrix[row][mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return False