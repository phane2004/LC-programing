class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        elif n < 1000000:
            return n - 999
        elif n < 1000000000:
            return (n - 999) + (n - (10 ** 6 - 1))
        elif n < 1000000000000:
            return (n - 999) + (n - (10 ** 6 - 1)) + (n - (10 ** 9 - 1))
        elif n < pow(10, 15):
            return (n - 999) + (n - (10 ** 6 - 1)) + (n - (10 ** 9 - 1)) + (n - (10 ** 12 - 1))
        else:
            return (n - 999) + (n - (10 ** 6 - 1)) + (n - (10 ** 9 - 1)) + (n - (10 ** 12 - 1)) + 1
