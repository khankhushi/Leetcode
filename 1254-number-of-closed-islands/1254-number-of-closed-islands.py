class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        
        def is_valid(r, c):
            return 0 <= r < R and 0 <= c < C
        
        def is_border(r, c):
            return r == 0 or r == R-1 or c == 0 or c == C-1
        
        def bfs(r, c):
            grid[r][c] = 1
            queue = collections.deque([(r, c)])
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if is_valid(nr, nc) and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr, nc))

        
        for r in range(R):
            for c in range(C):
                if is_border(r, c) and grid[r][c] == 0:
                    bfs(r, c)

        res = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    bfs(r, c)
                    res += 1
        return res