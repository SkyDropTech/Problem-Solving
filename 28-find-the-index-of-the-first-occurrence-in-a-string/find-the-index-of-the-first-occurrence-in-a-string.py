class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(haystack) 
        m=len(needle) 
        for i in range(n-m+1):
            res=haystack[i:i+m] 
            if res==needle:
                return i
                break 
        return -1