class Solution:
    def canConstruct(self, a: str, b: str) -> bool:
        freq={} 
        for i in b:
            if i not in freq:
                freq[i]=1 
            else:
                freq[i]+=1 
        for ch in a:
            if ch not in freq or freq[ch]==0 :
                return False
            freq[ch]-= 1 
        return True 
