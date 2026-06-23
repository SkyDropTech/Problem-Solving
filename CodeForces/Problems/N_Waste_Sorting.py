t=int(input())
res=""
for _ in range(t):
    c1,c2,c3=map(int,input().split())
    a1,a2,a3,a4,a5=map(int,input().split())

    if c1<a1 or c2<a2 or c3<a3:
        res+="NO\n"
        continue
    c1-=a1
    c2-=a2
    c3-=a3
    x=min(c1,a4)
    a4-=x
    x=min(c2,a5)
    a5-=x
    if a4+a5<=c3:
        res+="YES\n"
    else:
        res+="NO\n"
print(res)