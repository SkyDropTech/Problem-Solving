t=int(input())
res=""
for _ in range(t):
    w,h,n=map(int,input().split())
    count=1
    while w%2==0:
        w//=2
        count*=2 
    while h%2==0:
        h//=2
        count*=2 
    if count>=n:
        res+=str("YES")+"\n"
    else:
        res+=str("NO")+"\n"
print(res)