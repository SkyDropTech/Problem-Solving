class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n=len(nums)
        lst=[]
        s=set(nums)
        for i in range(1,n+1):
            if i not in s:
                lst.append(i) 
        return lst
                