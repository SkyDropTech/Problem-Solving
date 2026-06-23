t=int(input())
res=""
for _ in range(t):
    n=int(input())
    s=input().lower()
    com=s[0]
    for i in range(1,len(s)):
        if s[i]!=s[i-1]:
            com+=s[i]
    if com=="meow" :
        res+=str("YES")+"\n"
    else:
        res+=str("NO")+"\n"
print(res)
