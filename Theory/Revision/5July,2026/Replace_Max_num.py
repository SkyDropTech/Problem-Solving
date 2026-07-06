arr=list(map(int,input().split()))
ans=[0]*len(arr) 
maxi= -1 
for i in range(len(arr)-1,-1,-1):
    ans[i]=maxi
    if arr[i]>maxi:
        maxi=arr[i]
print(ans)
    