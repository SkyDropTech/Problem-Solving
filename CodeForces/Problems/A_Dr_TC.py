t=int(input())
res=""
for _ in range(t):
    n=int(input())
    a=input()
    for i in range(n):
        x=a.count("0")
        y=a.count("1")
    ans1=(1+y)*x 
    ans2=(y-1)*y 
    res+=str(ans1+ans2)+"\n"
print(res)