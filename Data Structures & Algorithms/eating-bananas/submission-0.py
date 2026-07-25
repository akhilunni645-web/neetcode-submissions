class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        from typing import List
  

        left = 1
        right = max(piles)

        result = right

        while left <= right:
            speed = (left + right) // 2

            hours = 0

            for pile in piles:
                hours += math.ceil(pile / speed)

            if hours <= h:
                result = speed
                right = speed - 1
            else:
                left = speed + 1

        return result