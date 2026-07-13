nums=[1, 2, 3, 4, 5]
n=len(nums)
k=3 
ans=0
for i in range(k):
    ans+=nums[i]
max_val=ans 
for i in range(1,n):
    ans-=nums[i-1] 
    ans+=nums[(i+k-1)%n] 
    if ans>max_val:
        max_val=ans 
print(max_val)