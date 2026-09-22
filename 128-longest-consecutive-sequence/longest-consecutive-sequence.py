class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums=sorted(set(nums))
        if len(nums)==0:
            return 0
        else:
            nums.append(-1) 
            maxi=0
            ct=1 
            for i in range(len(nums)-1):
                if nums[i+1]==nums[i]+1:
                    ct+=1 
                    maxi=max(maxi,ct)
                else: 
                    ct=1
            return max(maxi,ct)
