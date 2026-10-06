class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        trips = sorted(trips, key = lambda x : x[2])
        print(trips)
        n = trips[-1][2]
        li = [0] * (n + 1)

        for val, start, end in trips:
            li[start] += val
            li[end] -= val
        # print(li)
        for val in li:
            capacity -= val
            if capacity < 0:
                return False
        return True