import math
res=""
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    locked = 0
    
    for i in range(1, n-1):
        if math.gcd(a[i-1], a[i+1]) == a[i]:
            locked += 1
    
    res+=str(n - locked)+"\n"
print(res)