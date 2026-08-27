class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = [0] * 26

        # Count characters in s
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        n = len(s)
        i = 0

        # Match target prefix as long as possible
        while i < n:
            idx = ord(target[i]) - ord('a')

            if count[idx] == 0:
                break

            count[idx] -= 1
            i += 1

        # Try to increase at position i,
        # then backtrack to the left if needed
        while True:

            # Try replacing target[i] with
            # the smallest greater available character
            if i < n:
                curr = ord(target[i]) - ord('a')

                for j in range(curr + 1, 26):
                    if count[j] > 0:
                        count[j] -= 1

                        ans = target[:i] + chr(ord('a') + j)

                        # Append remaining characters in sorted order
                        for k in range(26):
                            ans += chr(ord('a') + k) * count[k]

                        return ans

            # No solution at this position
            # Move left and restore that character
            if i == 0:
                break

            i -= 1
            count[ord(target[i]) - ord('a')] += 1

        return ""