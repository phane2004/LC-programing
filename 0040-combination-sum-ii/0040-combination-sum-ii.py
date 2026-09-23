class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()
        def helper(s, st, temp):
            if s == 0:
                
                res.append(temp[:])
                return
            
            for i in range(st, len(candidates)):
                if candidates[i] > s:
                    break
                if i > st and candidates[i] == candidates[i - 1]:
                    continue
                temp.append(candidates[i])
                helper(s - candidates[i], i + 1, temp)
                temp.pop()
        helper(target, 0, [])
        return res
