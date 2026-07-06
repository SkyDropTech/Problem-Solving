n=int(input())
a=list(map(int,input().split()))
dp=[1]*n
for i in range(n-1):
    if a[i+1]>a[i]:
        dp[i+1]=dp[i]+1
    else:
        dp[i+1]=1 
print(max(dp))
