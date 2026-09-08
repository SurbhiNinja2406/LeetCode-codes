from collections import deque

class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        start_r, start_c = -1, -1
        total_keys = 0        
        for i in range(m):
            for j in range(n):
                ch = grid[i][j]
                if ch == '@':
                    start_r, start_c = i, j
                elif ch.islower():
                    total_keys += 1        
        all_keys_mask = (1 << total_keys) - 1  
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]        
        visited = set()
        start_state = (start_r, start_c, 0)
        visited.add(start_state)
        queue = deque([(start_r, start_c, 0, 0)])  
        while queue:
            r, c, keys_mask, steps = queue.popleft()
            if keys_mask == all_keys_mask:
                return steps            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue                
                cell = grid[nr][nc]
                if cell == '#':
                    continue                
                new_keys_mask = keys_mask
                if cell.isupper():
                    key_bit = 1 << (ord(cell.lower()) - ord('a'))
                    if not (keys_mask & key_bit):
                        continue  
                if cell.islower():
                    key_bit = 1 << (ord(cell) - ord('a'))
                    new_keys_mask = keys_mask | key_bit                
                new_state = (nr, nc, new_keys_mask)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((nr, nc, new_keys_mask, steps + 1))
        return -1
if __name__ == "__main__":
    sol = Solution()
    grid1 = ["@.a..", "###.#", "b.A.B"]
    result1 = sol.shortestPathAllKeys(grid1)
    print("Example 1:")
    print("Input: grid = {}".format(grid1))
    print("Output:", result1)
    print("Expected: 8")
    print()
    grid2 = ["@..aA", "..B#.", "....b"]
    result2 = sol.shortestPathAllKeys(grid2)
    print("Example 2:")
    print("Input: grid = {}".format(grid2))
    print("Output:", result2)
    print("Expected: 6")
    print()
    grid3 = ["@Aa"]
    result3 = sol.shortestPathAllKeys(grid3)
    print("Example 3:")
    print("Input: grid = {}".format(grid3))
    print("Output:", result3)
    print("Expected: -1")
print(__name__)