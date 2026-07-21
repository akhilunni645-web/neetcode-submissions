class Solution:
    def countBits(self, n: int) -> List[int]:
        

        # DP array to store the number of 1 bits
        dp = [0] * (n + 1)

        # Largest power of 2 seen so far
        offset = 1

        # Compute answers from 1 to n
        for i in range(1, n + 1):

            # Update offset when i becomes a power of 2
            if offset * 2 == i:
                offset = i

            # DP relation
            dp[i] = 1 + dp[i - offset]

        # Return the result
        return dp