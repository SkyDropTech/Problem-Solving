t=int(input())
res=""
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=int(input())
    a.sort() 
    if min(a)<=x<=max(a):
        res+="YES\n"
    else:
        res+="NO\n"
print(res)