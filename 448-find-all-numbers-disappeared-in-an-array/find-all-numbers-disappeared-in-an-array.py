class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums1=set(nums)
        res=[]
        for i in range(1,n+1):
            if i not in nums1:
                res.append(i)
        return res

