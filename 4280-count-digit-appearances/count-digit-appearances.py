class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        n=len(nums) 
        ct=0
        for i in range(n):
            s=str(nums[i]) 
            for j in range(len(s)):
                if s[j]==str(digit):
                    ct+=1
        return ct