 

class Solution:
    def combinationSum(self, nums, target):
        res = []

        def dfs(i, cur, total):

            # Found valid combination
            if total == target:
                res.append(cur.copy())
                return

            # Invalid path
            if i >= len(nums) or total > target:
                return

            # Include nums[i]
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # Backtrack
            cur.pop()

            # Skip nums[i]
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res