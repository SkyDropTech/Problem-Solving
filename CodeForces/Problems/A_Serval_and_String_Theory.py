t=int(input())
res=""
for _ in range(t):
    n,k=map(int,input().split())
    a=input().lower()

    if a < a[::-1]:
        res+="YES\n"
    else:
        if k>=1 and len(set(a))>1:
            res+="YES\n"
        else:
            res+="NO\n"
print(res)
