class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        def containDuplicate(nums):
            seen = set()

            for num in nums:
                if num in seen:
                    return True
                seen.add(num)
            return False
        return containDuplicate(nums)