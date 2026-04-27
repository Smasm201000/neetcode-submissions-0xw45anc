class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        l,h = 0,1
        for i in range(len(s) - 1):
            if s[h] > s[l]:
                total += ord(s[h]) - ord(s[l]) 
            else:
                total += ord(s[l]) - ord(s[h]) 

            l += 1
            h += 1
        return total