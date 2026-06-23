t = int(input())
res = ""

for _ in range(t):
    p, q = map(int, input().split())
    
    if p >= 2 and q >= 3 and 3*p >= 2*q and (p+q) % 2 == 0:
        res += "Bob\n"
    else:
        res += "Alice\n"

print(res)
