t=int(input())
res=""
for _ in range(t):
    n=int(input())
    b=n%2020 
    if  b<=n//2021:
        res+="YES\n"
    else:
        res+="NO\n"
print(res)
    
