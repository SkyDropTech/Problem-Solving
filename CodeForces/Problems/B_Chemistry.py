t=int(input())
res=""
for _ in range(t):
    n,k=map(int,input().split())
    s=input() 
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1 
    odd=0 
    for val in freq.values():
        if val%2!=0 :
            odd+=1 
    if k>=odd-1 : 
        res+="YES\n"
    else:
        res+="NO\n"
print(res)