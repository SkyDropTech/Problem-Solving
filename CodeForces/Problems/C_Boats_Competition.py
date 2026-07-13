t=int(input())
res=""
for _ in range(t):
    n=int(input())
    w=list(map(int,input().split()))
    i=0 
    j=n-1 
    freq={}
    while i<j:
        suum=w[i]+w[j]
        if suum not in freq:
            freq[suum]=1 
        else:
            freq[suum]+=1 
        i+=1 
        j-=1 
    ans=0
    for j in freq:
        if freq[j]>ans:
            ans=freq[j] 
    res+=str(ans)+"\n"
print(res)









