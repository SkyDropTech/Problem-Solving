class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # I probabily used AI in this question because i dont know what i have done or cannot understand the solution
        # So now lets solve this question using Hash Map or Table with optimized way 
        mp={} 
        left=0 
        ans=0 
        for right, ch in enumerate(s):
            if ch in mp:
                left=max(left,mp[ch]+1) 
            mp[ch]=right 
            ans=max(ans,right-left+1)
        return ans
        # res=""
        # max_val=0
        # for ch in s:
        #     while ch in res:
        #         res=res[1:] 
        #     res+=ch
        #     max_val=max(max_val,len(res))
        # return max_val

