class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int: 
        lst=[]
        for i in range(len(nums)):
            if nums[i]>0:
                lst.append(nums[i]) 
        lst.sort() 
        miss=1 
        for i in lst:
            if i==miss:
                miss+=1 
            elif i>miss:
                return miss
        return miss
