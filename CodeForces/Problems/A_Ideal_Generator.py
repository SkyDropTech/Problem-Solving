t=int(input())
res=""
for _ in range(t):
    k=int(input())
    if k%2==0:
        res+="NO\n" 
    else:
        res+="YES\n"
print(res)