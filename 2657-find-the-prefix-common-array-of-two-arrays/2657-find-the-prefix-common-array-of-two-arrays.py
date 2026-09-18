class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        exsist = set()
        count = 0
        res = []
        for i in range(len(A)):
            if A[i] in exsist:
                count += 1
            exsist.add(A[i])
            if B[i] in exsist:
                count += 1
            exsist.add(B[i])
            res.append(count)
        return res