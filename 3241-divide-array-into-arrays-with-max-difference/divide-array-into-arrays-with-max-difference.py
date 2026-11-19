class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        lst=[]
        ct=0
        for i in range(0,n-2,3):
            if abs(nums[i]-nums[i+1])<=k and abs(nums[i+1]-nums[i+2])<=k and abs(nums[i]-nums[i+2])<=k:
                lst.append([nums[i],nums[i+1],nums[i+2]])
                ct+=3
        if ct==n:
            return lst 
        return [] 

        