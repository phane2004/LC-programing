class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10 ** 9 + 7
        dp = 1
        prev = {}

        for ch in s:
            new_dp = 2 * dp - prev.get(ch, 0)
            prev[ch] = dp
            dp = new_dp % mod
        return (dp - 1) % mod