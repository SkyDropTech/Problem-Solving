class Solution:
    def beautySum(self, s: str) -> int:
        freq={} 
        ans=0
        n=len(s)
        for i in range(n):
            freq={} 
            for j in range(i,n):
                freq[s[j]]=freq.get(s[j],0)+1 

                maxi=max(freq.values()) 
                mini=min(freq.values()) 

                ans+=maxi-mini
        return ans