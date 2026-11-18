class Solution:
    def dividePlayers(self, nums: list[int]) -> int:
        nums.sort() 
        n=len(nums)
        lst=[]
        i=1
        j=n-2 
        ok=True
        suum=nums[0]+nums[n-1]
        while i<j:
            ans=nums[i]+nums[j] 
            if ans!=suum:
                ok=False
            else:
                lst.append(nums[i]*nums[j] ) 
            i+=1 
            j-=1
        konda=0

        if ok:
            lst.append(nums[0]*nums[n-1]) 
            for i in lst:
                konda+=i
        else:
            konda=-1 

        return konda
            