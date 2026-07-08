        

class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = -1


class Solution:

    def findWords(self, board, words):

        root = TrieNode()

        # Build Trie
        for i, word in enumerate(words):

            cur = root

            for c in word:

                if c not in cur.children:
                    cur.children[c] = TrieNode()

                cur = cur.children[c]

            cur.word = i

        ROWS = len(board)
        COLS = len(board[0])

        res = []
        visit = set()

        def dfs(r, c, node):

            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visit
                or board[r][c] not in node.children
            ):
                return

            visit.add((r, c))

            node = node.children[board[r][c]]

            if node.word != -1:

                res.append(words[node.word])

                node.word = -1

            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            visit.remove((r, c))

        for r in range(ROWS):

            for c in range(COLS):

                dfs(r, c, root)

        return res        