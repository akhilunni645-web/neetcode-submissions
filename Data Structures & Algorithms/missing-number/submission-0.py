class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        
        # Start with n
        res = len(nums)

        # XOR all indices and values
        for i in range(len(nums)):
            res ^= i
            res ^= nums[i]

        # The remaining value is the missing number
        return res