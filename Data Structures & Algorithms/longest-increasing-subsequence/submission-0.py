class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:


        memo = {}

        def dfs(i, prev):
            # Base case
            if i == len(nums):
                return 0

            # Memoized result
            if (i, prev) in memo:
                return memo[(i, prev)]

            # Skip current number
            skip = dfs(i + 1, prev)

            # Take current number (if valid)
            take = 0
            if prev == -1 or nums[i] > nums[prev]:
                take = 1 + dfs(i + 1, i)

            memo[(i, prev)] = max(skip, take)
            return memo[(i, prev)]

        return dfs(0, -1)
