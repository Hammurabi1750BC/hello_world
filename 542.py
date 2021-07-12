# 542	01 Matrix

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        mat2 = [[float('inf')] * len(mat[0]) for row in range(len(mat))]
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    mat2[row][col] = 0
                else:
                    if row > 0:
                        mat2[row][col] = min(mat2[row][col], mat2[row-1][col] + 1)
                    if col > 0:
                        mat2[row][col] = min(mat2[row][col], mat2[row][col -1] + 1)

        for row in range(len(mat)-1, -1, -1):
            for col in range(len(mat[0])-1, -1, -1):
                if mat[row][col] == 0:
                    mat2[row][col] = 0
                else:
                    if row < len(mat)-1:
                        mat2[row][col] = min(mat2[row][col], mat2[row+1][col] + 1)
                    if col < len(mat[0])-1:
                        mat2[row][col] = min(mat2[row][col], mat2[row][col +1] + 1)

        return mat2
