t=int(input())
res=""
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    lst=[]
    one=a.count(1) 
    for i in range(k):
        if a[i]>1:
            lst.append(a[i]) 
    m=0
    lst.sort() 
    if lst==[]:
        res+=str(one-1)+"\n"
    else:
        for j in range(len(lst)-1):
            m+=(lst[j]-1)+lst[j]  
        res+=str(m+one)+"\n"
print(res)