class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        trips = sorted(trips, key = lambda x : x[2])
        n = trips[-1][2]

        pre = [0] * (n + 1)

        for val, st, end in trips:
            pre[st] += val
            pre[end] -= val
        for i in range(n):
            if i != 0:
                pre[i] += pre[i - 1]
            if pre[i] > capacity:
                return False
        print(pre)
        return True