n,m=map(int,input().split())
s=[]
for i in range(n):
    s.append(input())
a=list(map(int,input().split()))

ans=0

for j in range(m):
    A=B=C=D=E=0 
    for i in range(n):
        if s[i][j]=="A":
            A+=1 
        elif s[i][j]=="B":
            B+=1
        elif s[i][j]=="C":
            C+=1
        elif s[i][j]=="D":
            D+=1
        else:
            E+=1
    maxx=max(A,B,C,D,E)
    ans+= maxx*a[j]
print(ans)
