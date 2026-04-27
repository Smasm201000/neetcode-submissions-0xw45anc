class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        for i in s:
            if i not in seen:
                seen[i] = 1
            seen[i] += 1
        seen_2 = {}
        for j in t:

            if j not in seen_2:
                seen_2[j] = 1
            seen_2[j] += 1

        return seen == seen_2  
            

        