n=int(input())
arr=list(map(int,input().split()))
k=int(input())
ans=0 
suum=0 
i=0 
for j in range(n):
    suum+=arr[j] 
    if j-i+1==k:
        ans=max(suum,ans)
        suum-=arr[i]
        i+=1 
print(ans)


