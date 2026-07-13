t=int(input())
res=""
for _ in range(t):
    n=int(input())
    w=list(map(int,input().split()))
    i=0
    j=n-1
    ans=0
    sum1=0
    sum2=0
    while i<=j:
        if sum1<=sum2: 
            sum1+=w[i]
            i+=1
        else:
            sum2+=w[j]
            j-=1 
        if sum1==sum2:
            ans=i+(n-j-1)
    res+=str(ans)+"\n"
print(res)
