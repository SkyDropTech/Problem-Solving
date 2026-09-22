class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1 
        for ch,i in enumerate(s):
            if freq[i]==1:
                return ch
                break 
        return -1