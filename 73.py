#73	Set Matrix Zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows, zero_cols = set(), set()
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)
                    
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in zero_rows or col in zero_cols:
                    matrix[row][col] = 0
                    
