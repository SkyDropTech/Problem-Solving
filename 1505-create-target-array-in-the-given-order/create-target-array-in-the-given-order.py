class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        n=len(nums)
        arr=[]
        for i in range(n):
            arr.insert(index[i],nums[i])
        return arr