n=int(input())
freq={}
for i in range(n):
    s=input() 
    if s in freq:
        freq[s]+=1 
        print(f"{s}{freq[s]-1}")
    else:
        freq[s]=1 
        print("OK")