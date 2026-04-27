class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = [i.lower() for i in s if i.isalpha() or i.isdigit()]
        
        l,h = 0,len(letters) - 1

        while l < h:   
              
            if letters[l] == letters[h]:
                l += 1
                h -= 1
            else:
                 
                return False
        return True

