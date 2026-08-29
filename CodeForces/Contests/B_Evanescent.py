t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    groups={}
    cnt=0
    groups[cnt]=s[0]
    for i in range(1,n):
        if s[i]!=s[i-1]:
            cnt+=1
            groups[cnt]=s[i]
    compressed=len(groups)
    ans=compressed
    for i in range(1,n-1):
        if s[i-1]==s[i+1]:
            if s[i]!=s[i-1]:
                ans=min(ans,compressed-2)
        elif s[i]!=s[i-1] and s[i]!=s[i+1]:
            ans=min(ans,compressed-1)
    print(ans)


    01001 
    00011 
    00110 
    10010 