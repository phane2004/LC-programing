class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        pre = defaultdict(list)

        for c, p in prerequisites:
            pre[c].append(p)
        vis = set()
        path = set()
        res = []
        def dfs(c):
            if c in path:
                return True
            if c in vis:
                return False
            vis.add(c)
            path.add(c)
            for p in pre[c]:
                if dfs(p):
                    return True
            path.remove(c)
            res.append(c)
            return False

        for course in range(numCourses):
            if dfs(course):
                return []
        
        return res