t=int(input())
res=""

for _ in range(t):
    n=int(input())
    s=input()

    # minimum
    mn=0
    i=0
    while i<n:
        if s[i]=='1':
            j=i
            while j<n and s[j]=='1':
                j+=1
            length=j-i
            mn+=(length+1)//2
            i=j
        else:
            i+=1

    # maximum
    pos=[i for i in range(n) if s[i]=='1']

    mx=0
    start=pos[0]

    for i in range(1,len(pos)):
        if pos[i]-pos[i-1]>=3:
            mx+=pos[i-1]-start+1
            start=pos[i]

    mx+=pos[-1]-start+1

    res+=str(mn)+" "+str(mx)+"\n"

print(res)