#1feb,2026 time 18:19
t=int(input())
res=""
for _ in range(t):
    lst=[]
    suum=0
    z=input().lower()
    s=input().lower()
    pos = {}
    for i, ch in enumerate(z):
        pos[ch] = i + 1

    for ch in s:
        if ch in pos:
            lst.append(pos[ch])
    for k in range(len(lst)-1):
         suum+=abs(lst[k]-lst[k+1])
    res+=str(suum)+"\n"
print(res)