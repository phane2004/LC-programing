class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num) // 2
        left = num[:n]
        right = num[n:]
        leftq = left.count('?')
        rightq = right.count('?')

        if(leftq + rightq) % 2 != 0:
            return True
        
        s1 = sum(map(int, left.replace('?', '0')))
        s2 = sum(map(int, right.replace('?', '0')))

        #print((2 * s1 + 9 * leftq),(2 * s2 + 9 * rightq))
        return (2 * s1 + 9 * leftq) != (2 * s2 + 9 * rightq)

        