class Solution:
    def compress(self, nums: list[str]) -> int:
        n=len(nums)
        nums.append(0) 
        ct=1
        lst=[]
        for i in range(n):
            if nums[i]==nums[i+1]:
                ct+=1
            elif nums[i]!=nums[i+1]:
                lst.append(nums[i])
                if ct>1:
                    for j in str(ct):
                        lst.append(j)
                ct=1
        for i in range(len(lst)):
            nums[i]=lst[i]

        return len(lst)





        