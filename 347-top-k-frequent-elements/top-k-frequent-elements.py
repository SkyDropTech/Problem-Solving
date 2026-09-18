class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq={} 
        for i in nums:
            freq[i]=freq.get(i,0)+1 
        elements = list(freq.keys())
        elements.sort(key=lambda x: freq[x], reverse=True)
        return elements[:k]
