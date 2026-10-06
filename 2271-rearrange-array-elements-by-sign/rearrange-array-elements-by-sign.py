class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n=len(nums) 
        num=[0]*n 
        pos=0 
        neg=1 
        for ch in nums:
            if ch>0:
                num[pos]=ch 
                pos+=2 
            else:
                num[neg]=ch 
                neg+=2 
        return num
        