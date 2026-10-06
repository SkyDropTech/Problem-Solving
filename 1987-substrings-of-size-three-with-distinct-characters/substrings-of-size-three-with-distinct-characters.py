class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n=len(s)
        ct=0
        for i in range(n-2):
            res=s[i:i+3]
            if len(set(res))==3:
                ct+=1 
        return ct

