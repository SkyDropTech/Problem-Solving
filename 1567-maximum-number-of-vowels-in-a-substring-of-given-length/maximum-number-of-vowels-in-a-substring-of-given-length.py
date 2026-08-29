class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ct=0
        for i in range(k):
            if s[i] in "aeiou":
                ct+=1 
        max_num=ct 
        for i in range(k,len(s)):
            if s[i-k] in "aeiou":
                ct-=1 
            if s[i] in "aeiou":
                ct+=1 
            max_num=max(max_num,ct)
        return max_num


            