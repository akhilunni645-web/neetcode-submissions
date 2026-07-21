class Solution:
    def getSum(self, a: int, b: int) -> int:
        

        # 32-bit mask
        MASK = 0xFFFFFFFF

        # Maximum positive 32-bit integer
        MAX = 0x7FFFFFFF

        # Continue until there is no carry
        while b != 0:

            # Sum without carry
            temp = (a ^ b) & MASK

            # Carry
            b = ((a & b) << 1) & MASK

            # Update a
            a = temp

        # If positive, return directly
        if a <= MAX:
            return a

        # Convert from two's complement to negative
        return ~(a ^ MASK)