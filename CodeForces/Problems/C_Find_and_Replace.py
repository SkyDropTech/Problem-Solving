t=int(input())
res=""
for _ in range(t):
    n=int(input())
    s=input().lower()

    lst1=s[0:n:2]
    lst2=s[1:n:2]

    found= False
    for ch in lst1:
        if ch in lst2:
            found=True 
            break 
    if found:
        res+="NO\n"
    else:
        res+="YES\n"
print(res)