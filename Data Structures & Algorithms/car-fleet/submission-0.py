class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        


        # Pair each car's position with its speed
        cars = list(zip(position, speed))

        # Sort by position from nearest to farthest
        cars.sort(reverse=True)

        # Stack stores fleet arrival times
        stack = []

        # Process each car
        for pos, spd in cars:

            # Time required to reach target
            time = (target - pos) / spd

            # If current car cannot catch fleet ahead,
            # it forms a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)

            # Else:
            # Current car joins the fleet ahead.
            # Do nothing.

        return len(stack)