class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n=len(nums)
        arr=[0]*n
        for i in range(n):
            ct=0
            for j in range(n):
                if nums[i]>nums[j]:
                    ct+=1 
            arr[i]=ct 
        return arr


