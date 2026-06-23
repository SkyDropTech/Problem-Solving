t=int(input())
res=""
for _ in range(t):
    l,r,a=map(int,input().split())
    x1=r//a+r%a
    x2=(r//a)*a-1
    if x2>=l:
        x2v=x2//a + x2%a
        ans=max(x1,x2v)
    else:
        ans=x1
    res+=str(ans)+"\n"
print(res)