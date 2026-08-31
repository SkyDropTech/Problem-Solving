class Solution:
    def firstUniqChar(self, s: str) -> int:
        #More optimized way to solve this question
        freq={} 
        for i in s:
            freq[i]=freq.get(i,0)+1 
        for i,x in enumerate(s):
            if freq[x]==1:
                return i 
                break 
        return -1
        # freq = {}
        # for ch in s:
        #     if ch in freq:
        #         freq[ch] += 1
        #     else:
        #         freq[ch] = 1
        # for i in range(len(s)):
        #     if freq[s[i]] == 1:
        #         return i
        # return -1