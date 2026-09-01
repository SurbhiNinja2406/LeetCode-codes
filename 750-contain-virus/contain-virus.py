class Solution(object):
    def containVirus(self, isInfected):
        """
        :type isInfected: List[List[int]]
        :rtype: int
        """
        if not isInfected or not isInfected[0]:
            return 0        
        m, n = len(isInfected), len(isInfected[0])
        total_walls = 0        
        def neighbors(r, c):
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    yield nr, nc        
        while True:
            visited = [[False]*n for _ in range(m)]
            regions = [] 
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and not visited[i][j]:
                        stack = [(i, j)]
                        visited[i][j] = True
                        cells = set()
                        frontier = set()
                        walls = 0                        
                        while stack:
                            r, c = stack.pop()
                            cells.add((r, c))
                            for nr, nc in neighbors(r, c):
                                if isInfected[nr][nc] == 1:
                                    if not visited[nr][nc]:
                                        visited[nr][nc] = True
                                        stack.append((nr, nc))
                                elif isInfected[nr][nc] == 0:
                                    frontier.add((nr, nc))
                                    walls += 1  
                        regions.append({'cells': cells, 'frontier': frontier, 'walls': walls})            
            if not regions:
                break
            if max(len(r['frontier']) for r in regions) == 0:
                break
            regions.sort(key=lambda r: len(r['frontier']), reverse=True)
            worst = regions[0]
            total_walls += worst['walls']
            for r, c in worst['cells']:
                isInfected[r][c] = 2 
            for region in regions[1:]:
                for r, c in region['frontier']:
                    isInfected[r][c] = 1        
        return total_walls
print(__name__)