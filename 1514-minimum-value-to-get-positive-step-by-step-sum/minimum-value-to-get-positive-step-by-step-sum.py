class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n=len(nums)
        arr=[0]*(n+1)
        suum=arr[0] 
        mini=float('inf')
        for i in range(1,n+1):
            suum+=nums[i-1]
            arr.append(suum)
        return abs(min(arr)-1)


    