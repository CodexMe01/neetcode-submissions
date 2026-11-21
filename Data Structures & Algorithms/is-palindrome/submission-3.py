class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = "".join(filter(str.isalnum, "".join(s.lower().split())))
        n = len(l)
        if l[:((n//2)+1)] == l[-((n//2)+1):][::-1]:
            return True
        else: 
            return False

        