class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        

        # Count frequency of each task
        freq = [0] * 26

        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        # Highest frequency
        maxFreq = max(freq)

        # Number of tasks having the highest frequency
        maxFreqCount = freq.count(maxFreq)

        # Minimum cycles considering idle time
        intervals = (maxFreq - 1) * (n + 1) + maxFreqCount

        # We cannot need fewer cycles than the number of tasks
        return max(len(tasks), intervals)