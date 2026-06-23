t=int(input())
for _ in range(t):
    a=int(input())
    p=180-a 
    b=2*a 
    if b%p==0:
        print("YES")
    else:
        print("NO")