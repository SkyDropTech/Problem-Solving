class Solution:
    def defangIPaddr(self, s: str) -> str:
        res=""
        for i in range(len(s)):
            if s[i]==".":
                res+=f"[{s[i]}]"
            else:
                res+=f"{s[i]}" 
        return res
