class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        n=len(nums) 
        lst=[]
        for i in range(len(l)):
            value=nums[l[i]:r[i]+1] 
            value.sort()
            ok=True
            x=abs(value[1]-value[0])
            for i in range(1,len(value)-1):
                if abs(value[i]-value[i+1])!=x:
                    ok=False
            if ok:
                lst.append(True) 
            else:
                lst.append(False)
        return lst