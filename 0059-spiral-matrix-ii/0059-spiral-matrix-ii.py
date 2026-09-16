class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        print(matrix)

        u, r, d, l = 0, n - 1, n - 1, 0
        up, ri, dn, le = 0, 1, 0, 0
        num = 1
        while num <= n * n:

            if ri:
                for col in range(l, r + 1):
                    # print(num, u, col)
                    matrix[u][col] = num
                    num += 1
                ri = 0
                dn = 1
                u += 1
            elif dn:
                for row in range(u, d + 1):
                    matrix[row][r] = num
                    num += 1
                dn = 0
                le = 1
                r -= 1
            elif le:
                for col in range(r, l - 1, -1):
                    matrix[d][col] = num
                    num += 1
                le = 0
                up = 1
                d -= 1
            elif up:
                for row in range(d, u - 1, -1):
                    matrix[row][l] = num
                    num += 1
                up = 0
                ri = 1
                l += 1
            # print(matrix)
        return matrix
