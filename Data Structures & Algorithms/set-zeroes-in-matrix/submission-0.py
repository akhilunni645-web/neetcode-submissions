class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        
        from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])

        # Tracks whether the first row should be zeroed
        rowZero = False

        # Step 1: Use first row and first column as markers
        for r in range(rows):
            for c in range(cols):

                if matrix[r][c] == 0:

                    if r == 0:
                        rowZero = True
                    else:
                        matrix[r][0] = 0

                    matrix[0][c] = 0

        # Step 2: Update the inner matrix (excluding first row and first column)
        for r in range(1, rows):
            for c in range(1, cols):

                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Step 3: Update the first column
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        # Step 4: Update the first row
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0