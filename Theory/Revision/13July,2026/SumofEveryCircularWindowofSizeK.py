nums=[5,2,-3,4,1]
n=len(nums) 
k=3 
suum=0
for i in range(k):
    suum+=nums[i] 
print(suum)
for i in range(1,n):
    suum=suum-nums[i-1] 
    suum=suum+nums[(i+k-1)%n] 
    print(suum)
