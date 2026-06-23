t=int(input())
res=""
for _ in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    
    marked=[False]*(n+1)
    count=0
    
    for i in range(n):
        chair=i+1
        if marked[chair]:
            break
        target=p[i]
        if target<=chair:
            count+=1
            marked[target]=True
    
    res+=f"{count}\n"
print(res)