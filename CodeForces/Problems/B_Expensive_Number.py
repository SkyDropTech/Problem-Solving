t=int(input())
res=""
for _ in range(t):
    n=input()
    s=len(n)
    zero_count=0
    max_count=0 
    for i in range(s):
        if n[i]=="0":
            zero_count+=1 
        else:
            max_count=max(max_count,zero_count+1)
    ans=s-max_count 
    res+=str(ans)+"\n"
print(res)