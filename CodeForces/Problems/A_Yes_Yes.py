t=int(input())
res=""
pattern="Yes"*100 
for _ in range(t):
    s=input()
    if s in pattern:
        res+="YES\n"
    else:
        res+="NO\n"
print(res)                                              