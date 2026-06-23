t=int(input())
res=""
for _ in range(t):
    s=input().upper()
    T=False
    for i in range(len(s)):
        x=s.count(s[i])
        if s.count("Y")>1:
            T=True
    if T:
        res+="NO\n"
    else:
        res+="YES\n"
print(res)
        
