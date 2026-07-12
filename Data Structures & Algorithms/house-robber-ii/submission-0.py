class Solution:
    def rob(self, nums: List[int]) -> int:
        

    
        if len(nums) == 1:
            return nums[0]

        def robLine(houses):

            rob1 = 0
            rob2 = 0

            for money in houses:

                temp = max(money + rob1, rob2)

                rob1 = rob2
                rob2 = temp

            return rob2

        return max(
            robLine(nums[:-1]),
            robLine(nums[1:])
        )