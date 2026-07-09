class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        

        # Step 1: Create graph
        graph = {char: set() for word in words for char in word}

        # Step 2: Build edges
        for i in range(len(words) - 1):

            word1 = words[i]
            word2 = words[i + 1]

            # Invalid prefix case
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            minLen = min(len(word1), len(word2))

            for j in range(minLen):

                if word1[j] != word2[j]:
                    graph[word1[j]].add(word2[j])
                    break

        visited = {}
        result = []

        def dfs(char):

            # Cycle detected
            if char in visited:
                return visited[char]

            visited[char] = True

            for neighbor in graph[char]:
                if dfs(neighbor):
                    return True

            visited[char] = False

            result.append(char)

            return False

        # DFS for every character
        for char in graph:

            if dfs(char):
                return ""

        result.reverse()

        return "".join(result)