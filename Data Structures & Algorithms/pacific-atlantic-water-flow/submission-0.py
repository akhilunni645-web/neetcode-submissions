class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        ROWS = len(heights)
        COLS = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visit, prevHeight):

            # Outside grid
            if (
                r < 0 or
                c < 0 or
                r == ROWS or
                c == COLS
            ):
                return

            # Already visited
            if (r, c) in visit:
                return

            # Reverse water flow condition
            if heights[r][c] < prevHeight:
                return

            visit.add((r, c))

            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Pacific (top row)
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])

        # Pacific (left column)
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])

        # Atlantic (bottom row)
        for c in range(COLS):
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        # Atlantic (right column)
        for r in range(ROWS):
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res