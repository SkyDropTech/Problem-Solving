n=int(input())
a=input().upper()
freq={}
for i in range(n-1):
    pair=a[i]+a[i+1]
    if pair in freq:
        freq[pair]+=1
    else:
        freq[pair]=1
        
max_pair=""
max_count=0

for key in freq:
    if freq[key] > max_count:
        max_count = freq[key]
        max_pair = key

print(max_pair)



    