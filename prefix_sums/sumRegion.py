from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        if n == 0:
            return
        m = len(matrix[0])
        self.prefix_matrix = [[0] * m for _ in range(n)]
        for i in range(n):
            cur_row = 0
            for j in range(m):
                cur_row += matrix[i][j]
                self.prefix_matrix[i][j] = cur_row + (0 if i-1 < 0 else self.prefix_matrix[i-1][j])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # F(y1,x1, y2,x2) = f(y2,x2) - f(y1-1,x2) - (f(y2,x1-1)-f(y1-1,x1-1))
        # F = a - b - (x, y)
        # print(self.prefix_matrix)
        a = self.prefix_matrix[row2][col2]
        b = 0 if row1 - 1< 0 else self.prefix_matrix[row1-1][col2]
        x = 0 if col1 - 1 < 0 else self.prefix_matrix[row2][col1-1]
        y = 0 if row1 - 1 < 0 or col1 - 1 < 0 else self.prefix_matrix[row1-1][col1-1]
        return a - b - (x - y)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)