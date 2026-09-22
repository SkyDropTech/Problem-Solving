class Solution:
    def reverseString(self, s: list[str]) -> None:
        res=""
        lst=[] 
        for i in s:
            res+=i 
        res=res[::-1] 
        for i in res:
            lst.append(i) 
        s[:]=lst