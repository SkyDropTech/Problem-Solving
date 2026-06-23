a=input()
b=input() 
x=int(a)+int(b)
tot=int(a)+int(b)
a=a.replace("0", "")
b=b.replace("0", "")
tot1=int(a)+int(b)
tot1=str(tot1)
tot=str(tot)
tot=tot.replace("0", "")

if tot==tot1:
    print("YES")
else:
    print("NO")