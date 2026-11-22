class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        spaces.append(0) 
        spaces.append(len(s))
        spaces.sort()
        
        res=""
        for i in range(len(spaces)-1):
            res+=(s[spaces[i]:spaces[i+1]])+" "
        return res.rstrip()