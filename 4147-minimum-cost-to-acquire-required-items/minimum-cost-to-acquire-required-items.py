class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        maxi=max(need1,need2) 
        mini=min(need1,need2) 
        if need1>need2:
            ans3=mini*costBoth+abs(need1-need2)*cost1
        else:
            ans3=mini*costBoth+abs(need1-need2)*cost2
        ans1=maxi*costBoth 
        ans2=cost1*need1+cost2*need2 
        return min(ans1,ans2,ans3)


