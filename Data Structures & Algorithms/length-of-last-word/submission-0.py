class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        text = s.strip().split(" ")
        for i in range(len(text)):
            count = len(text[-1])
        return count