class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        pre = [0] * n

        for s, e, val in bookings:
            pre[s - 1] += val
            if e < n:
                pre[e] -= val
        for i in range(1, n):
            pre[i] += pre[i - 1]
        return pre