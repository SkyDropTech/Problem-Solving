
class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n=len(nums)
        lst1=[]
        suum_first=sum(nums[:n//2])
        lst1.append(suum_first)
        for i in range(1,n):
            suum_first=suum_first-nums[(i-1)%n]+nums[(i+n//2-1)%n]
            lst1.append(suum_first)
        lst2=[]
        suum_sec=sum(nums[n//2:])
        lst2.append(suum_sec)
        for i in range(1,n):
            suum_sec=suum_sec-nums[(i+n//2-1)%n]+nums[(i-1)%n]
            lst2.append(suum_sec)
        ct=0
        for i in range(len(lst1)):
            if lst1[i]>lst2[i]:
                ct+=1
        return ct
