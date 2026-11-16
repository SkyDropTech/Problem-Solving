class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n=len(nums) 
        maxi=max(nums) 
        mini=min(nums) 
        lst=[]
        for i in range(n):
            if nums[i]==maxi:
                lst.append(i+1)
            if nums[i]==mini:
                lst.append(i+1) 
        lst.sort()
        a=lst[1]
        b=n-lst[0]+1
        c=lst[0]+n-lst[1]+1

        return min(a,b,c)


