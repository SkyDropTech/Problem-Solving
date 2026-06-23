t=int(input())
res=""
for _ in range(t):
    n=int(input())
    X=False
    a=list(map(int,input().split()))
    if 67 in a and 1 in a :
        res+="YES\n"
    else:
        res+="NO\n"
print(res)