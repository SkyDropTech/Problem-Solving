class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans=""
        ct=0
        for i in range(len(s)-2):
            ans=s[i:i+3]
            if ans[0]!=ans[1] and ans[1]!=ans[2] and ans[0]!=ans[2] :
                ct+=1 
        return ct


