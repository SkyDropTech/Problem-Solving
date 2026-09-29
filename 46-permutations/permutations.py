class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        from itertools import permutations

        ans = []

        for p in permutations(nums):
            ans.append(list(p))

        return ans