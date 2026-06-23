t=int(input())
res=""
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n):
        if a.count(a[i])==1:
            res+=str(i+1)+"\n"
print(res)