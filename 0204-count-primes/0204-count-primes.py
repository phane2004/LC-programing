class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        bool = [True] * n

        for i in range(2, int(n ** 0.5) + 1):
            if bool[i]:
                for j in range(i * i, n, i):
                    bool[j] = False
        return sum(bool[2:])