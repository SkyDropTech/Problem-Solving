t = int(input())
res=""
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans=0
    for s in range(2,101):
        i=0 
        j=n-1 
        count=0
        while i<j:
            total=a[i]+a[j]
            if total==s:
                count+=1 
                i+=1 
                j-=1 
            elif total<s:
                i+=1 
            else:
                j-=1 
        if count>ans:
            ans=count 
    print(ans)


