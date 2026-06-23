n=int(input())
res=""
times=[]
for _ in range(n):
    h,m=map(int,input().split())
    times.append((h,m))
ct=1
max_ct=1
for i in range(n-1):
    if times[i]==times[i+1]:
        ct+=1
        max_ct=max(ct,max_ct)
    else:
        ct=1
print(max_ct)