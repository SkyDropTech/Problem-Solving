class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=""
        max_val=0
        for ch in s:
            while ch in res:
                res=res[1:] 
            res+=ch
            max_val=max(max_val,len(res))
        return max_val

