
from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        # redo it
        def digit_sum(x):
            total = 0
            while x > 0:
                total += x % 10
                x //= 10
            return total

        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        target_index = {value: i for i, value in enumerate(sorted_nums)}
        #print(sorted_nums, target_index)
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or target_index[nums[i]] == i:
                visited[i] = True
                continue

            cycle_length = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = target_index[nums[j]]
                cycle_length += 1

            swaps += cycle_length - 1

        return swaps
