class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        n = len(temperatures)

        # Result array initialized with 0
        result = [0] * n

        # Stack stores indices
        stack = []

        # Traverse all temperatures
        for i in range(n):

            # While current temperature is warmer
            while stack and temperatures[i] > temperatures[stack[-1]]:

                # Previous colder day's index
                prev = stack.pop()

                # Days waited
                result[prev] = i - prev

            # Push current index
            stack.append(i)

        return result