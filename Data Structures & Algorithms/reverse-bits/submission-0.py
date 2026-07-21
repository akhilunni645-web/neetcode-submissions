class Solution:
    def reverseBits(self, n: int) -> int:
        

        # Store the reversed number
        res = 0

        # Check all 32 bits
        for i in range(32):

            # Extract the i-th bit
            bit = (n >> i) & 1

            # If the bit is 1, place it at the reversed position
            if bit:
                res |= (1 << (31 - i))

        # Return the reversed number
        return res