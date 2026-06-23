# t = int(input())
# for _ in range(t):
#     n = int(input())
    
#     if n & (n-1) == 0:
#         print("NO")
#     else:
#         print("YES")
t = int(input())
res=""
for _ in range(t):
    n=int(input())
    while n%2==0:
        n//=2
    if n==1:
        res+="NO\n"
    else:
        res+="YES\n"
print(res)