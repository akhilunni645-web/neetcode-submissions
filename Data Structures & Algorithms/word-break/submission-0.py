class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        memo = {}

        def dfs(i):
            # Base case
            if i == len(s):
                return True

            # Already computed
            if i in memo:
                return memo[i]

            # Try every word
            for word in wordDict:
                if s.startswith(word, i):
                    if dfs(i + len(word)):
                        memo[i] = True
                        return True

            memo[i] = False
            return False

        return dfs(0)