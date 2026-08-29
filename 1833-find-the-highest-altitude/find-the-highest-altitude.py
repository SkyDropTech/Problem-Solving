class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_sum=0 
        curr_sum=0
        for i in gain:
            curr_sum+=i 
            max_sum=max(curr_sum,max_sum)
        return max_sum