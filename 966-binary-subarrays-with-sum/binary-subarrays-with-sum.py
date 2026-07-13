class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def solve(k):
            if k < 0:
                return 0
            i = 0
            suum = 0
            ans = 0
            for j in range(len(nums)):
                suum += nums[j]

                while suum > k:
                    suum -= nums[i]
                    i += 1

                ans += j - i + 1

            return ans

        return solve(goal) - solve(goal-1)