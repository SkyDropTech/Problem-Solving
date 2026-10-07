class Solution:
    def scoreOfString(self, s: str) -> int:
        n=len(s)
        suum=0
        for i in range(n-1):
            suum+=abs(ord(s[i])-ord(s[i+1]))
        return suum
