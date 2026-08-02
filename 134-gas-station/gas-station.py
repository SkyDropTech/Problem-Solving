class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas) 
        total_gas=sum(gas) 
        total_cost=sum(cost) 
        curr=0 
        start=0 
        for i in range(n):
            curr+=gas[i]-cost[i] 
            if curr<0:
                curr=0 
                start=i+1 
        if total_gas<total_cost:
            return -1 
        return start