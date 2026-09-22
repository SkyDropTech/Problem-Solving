class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        suum=0 
        arr=[]
        for i in range(len(nums)):
            suum+=nums[i]
            arr.append(suum) 
        return arr
            