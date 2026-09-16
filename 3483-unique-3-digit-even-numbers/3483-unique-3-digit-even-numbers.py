class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = Counter(digits)
        count = 0

        for num in range(100, 999, 2):

            u, r = divmod(num, 100)
            t, tr = divmod(r, 10)

            count += freq[u] > 0 and freq[t] > (u == t) and freq[tr] > (u == tr) + (t == tr)
        return count