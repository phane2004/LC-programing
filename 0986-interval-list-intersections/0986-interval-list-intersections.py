class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        res = []

        for s, e in firstList:
           # print(s, e)
            for s1, e1 in secondList:
                #print("m", s1, e1)
                if e >= s1 and s <= e1:
                    res.append([max(s, s1), min(e, e1)])
        return res
