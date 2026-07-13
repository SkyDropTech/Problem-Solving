nums=[5,2,-3,4,1]
n=len(nums)
target=4 
j=0 
for i in range(len(nums)):
    if nums[i]==target:
        j=i 
        break 
for i in range(len(nums)):
    print(nums[(j+i)%n],end=" ")