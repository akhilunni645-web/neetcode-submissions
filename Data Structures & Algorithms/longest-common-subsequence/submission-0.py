class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m = len(text1)
        n = len(text2)

        # Create DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill table from bottom-right
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                # Characters match
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]

                # Characters don't match
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]