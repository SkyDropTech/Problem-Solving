arr=list(map(int,input().split()))
n=len(arr)
# prefix minimum from left 
# prefix maximum from right 
right=[0]*n
left=[0]*n

left[0]=arr[0]
right[n-1]=arr[n-1] 

for i in range(1,len(arr)):
    left[i]=min(arr[i],left[i-1])

for i in range(len(arr)-2,-1,-1):
    right[i]=max(arr[i],right[i+1])

i=0 
j=0 
ans=0
while i<n and j<n:
    if left[i]<=right[j]:
        ans=max(ans,j-i)
        j+=1 
    else:
        i+=1 
print(ans)

