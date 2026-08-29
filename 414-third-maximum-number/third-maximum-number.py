class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s=set(nums) 
        n=len(s)
        lst=list(s)
        lst.sort()
        if len(s)<3:
            return max(s) 
        else:
            return lst[n-3]