class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        l,h = 0,1
        for i in range(len(s) - 1):
            total += abs(ord(s[h]) - ord(s[l]) )
            l += 1
            h += 1
        return total