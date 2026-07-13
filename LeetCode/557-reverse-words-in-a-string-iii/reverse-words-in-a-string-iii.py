class Solution:
    def reverseWords(self, m: str) -> str:
        s=m.split() 
        res="" 
        for i in s:
            res+=i[::-1]+" "
        return res.strip()