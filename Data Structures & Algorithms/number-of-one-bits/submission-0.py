class Solution:
    def hammingWeight(self, n: int) -> int:
        

        # Store the number of 1 bits
        count = 0

        # Continue until all set bits are removed
        while n:

            # Remove the rightmost set bit
            n = n & (n - 1)

            # Increment count
            count += 1

        # Return total number of 1 bits
        return count