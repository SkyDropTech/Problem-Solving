t=int(input()) 
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    freq={} 
    res=""
    ct=0
    for i in range(n):
        key=a[i]-i 
        if key in freq:
            ct+=freq[key] 
            freq[key]+=1 
        else:
            freq[key]=1 
    res=f"{ct}"
    print(res)
