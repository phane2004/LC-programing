class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        # print(v1, v2)
        if len(v1) < len(v2):
            count = len(v2) - len(v1)
            v1.extend(['0'] * count)
        elif len(v2) < len(v1):
            count = len(v1) - len(v2)
            v2.extend(['0'] * count)

        for i in range(len(v1)):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
        return 0