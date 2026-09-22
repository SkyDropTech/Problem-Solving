class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        arr1=[] 
        arr2=[]
        n=len(nums)
        for i in range(n):
            if nums[i]%2==0:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        return arr1+arr2