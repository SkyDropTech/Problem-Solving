class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n=len(nums) 
        j=n-1 
        i=0 
        while i<j:
            if nums[i]+nums[j]==target:
                return [i+1,j+1] 
                break
            elif nums[i]+nums[j]>target:
                j-=1 
            else:
                i+=1 
