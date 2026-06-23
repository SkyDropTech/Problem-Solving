k=int(input())
s=input().lower() 
freq={} 
for ch in s:
    if ch in freq:
        freq[ch]+=1 
    else:
        freq[ch]=1 
for ch in freq:
    if freq[ch]%k!=0:
        print(-1)
        exit()
t="" 
for ch in freq:
    t+=ch*(freq[ch]//k)
print(t*k)