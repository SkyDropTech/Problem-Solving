arr=list(map(int,input().split()))
n=len(arr)
left=[0]*n
right=[0]*n

left[0]=arr[0] 
for i in range(1,len(arr)):
    left[i]=max(arr[i],left[i-1])

right[n-1]=arr[n-1] 
for i in range(len(arr)-2,-1,-1):
    right[i]=max(arr[i],right[i+1])

ans=0
for i in range(n):
    ans+=(min(left[i],right[i]))-arr[i]
print(ans)