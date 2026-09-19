class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        freq={} 
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]]=[] 
            freq[s[i]].append(t[i]) 
        
        for ch in freq:
            if len(set(freq[ch]))!=1:
                return False
        freq={}
        for i in range(len(s)):
            if t[i] not in freq:
                freq[t[i]]=[] 
            freq[t[i]].append(s[i]) 
        
        for ch in freq:
            if len(set(freq[ch]))!=1:
                return False
        return True 
