class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def dfs(rem):
            # Base case
            if rem == 0:
                return 0

            if rem < 0:
                return float("inf")

            # Already computed
            if rem in memo:
                return memo[rem]

            ans = float("inf")

            # Try every coin
            for coin in coins:
                ans = min(ans, 1 + dfs(rem - coin))

            memo[rem] = ans
            return ans

        result = dfs(amount)

        if result == float("inf"):
            return -1
        return result