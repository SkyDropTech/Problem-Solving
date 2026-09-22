class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq={} 
        ct=0
        ok=False
        for ch in s:
            freq[ch]=freq.get(ch,0)+1 
        for i in freq:
            if freq[i]%2!=0:
                ct+=(freq[i])-1
                ok=True 
            else:
                ct+=freq[i] 
        if ok:
            return ct+1 
        else:
            return ct
            
            
