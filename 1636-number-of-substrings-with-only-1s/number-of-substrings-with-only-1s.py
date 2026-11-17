class Solution:
    def numSub(self, s: str) -> int:
        n=len(s) 
        ans=0 
        ct=0 
        mod=10**9 + 7
        for i in range(n):
            if s[i]=="1":
                ct+=1 
            else:
                ct=0 
            ans=(ans+ct)%mod
        return ans


        # O(n^3)
        # n=len(s) 
        # left=0 
        # ans=0
        # while left<n:
        #     right=left 
        #     while right<n:
        #         x=s[left:right+1] 
        #         ct=x.count("1") 
        #         if ct==len(x):
        #             ans+=1 
        #         right+=1 
        #     left+=1 
        # return ans
        