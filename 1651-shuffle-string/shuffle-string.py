class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dict={}
        for i in range(len(s)):
            dict[indices[i]]=s[i]
        res=""
        x=sorted(dict.keys())
        for i in x:
            res+=str(dict[i])
        return res