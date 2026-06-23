n=int(input())
a=list(map(int,input().split()))
x=sorted(a,reverse=True)

lst=[]
ans=0
for i in range(1,n):
    aws=(x[i]*i)+1
    lst.append(i)
    ans+=aws 
print(ans+1)
idx=list(range(1,n+1))
idx.sort(key=lambda i:(-a[i-1],-i))

print(*idx)
