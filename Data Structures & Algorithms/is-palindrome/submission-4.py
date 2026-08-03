class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum,s))
        s = s.lower()
        n = len(s)
        return s[0:int(n/2)] == s[-1:int((n+1)/2)-1:-1]