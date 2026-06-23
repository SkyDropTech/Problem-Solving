t=int(input())
res=""
for _ in range(t):
    damage=0
    max_attack=0
    A,B,n=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(n):
        hits = (b[i] + A - 1) // A
        damage += hits * a[i]
        max_attack = max(max_attack, a[i])
    if B > damage - max_attack:
        res+="YES\n"
    else:
        res+="NO\n"
        
print(res)