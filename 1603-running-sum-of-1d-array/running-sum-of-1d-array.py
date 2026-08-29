class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr=[] 
        suum=0
        for i in range(len(nums)):
            suum+=nums[i] 
            arr.append(suum) 
        return arr