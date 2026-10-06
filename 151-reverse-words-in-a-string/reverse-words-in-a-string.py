class Solution:
    def reverseWords(self, s: str) -> str:
        lst=[] 
        s=s+" " 
        res=""
        for i in range(len(s)):
            if s[i]==" " and res=="":
                continue
            if s[i]==" ":
                lst.append(res)
                res=""
            else:
                res+=s[i]
        lst=lst[::-1] 
        res="" 
        for i in range(len(lst)-1):
            res+=lst[i] 
            res+=" "
        res=res+lst[-1]
        return res