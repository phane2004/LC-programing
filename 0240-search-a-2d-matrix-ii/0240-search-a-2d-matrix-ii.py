class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        r = 0
        c = col - 1

        while r < row and c > -1:

            if matrix[r][c] == target:
                return True

            elif matrix[r][c] < target:
                r += 1
            else:
                c -= 1
        return False
