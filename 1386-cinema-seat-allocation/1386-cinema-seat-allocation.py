class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        rows = {}

        for r, seat in reservedSeats:
            if r not in rows:
                rows[r] = set()
            rows[r].add(seat)

        ans = 2 * n

        for seats in rows.values():

            left = not any(s in seats for s in range(2, 6))
            middle = not any(s in seats for s in range(4, 8))
            right = not any(s in seats for s in range(6, 10))

            if left and right:
                continue

            ans -= 1

            if middle:
                continue

            if left or right:
                continue

            ans -= 1

        return ans