class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()
        for i in range(len(grid)):
            for k in range(len(grid[i])) :
                if grid[i][k] in visited :
                    continue
                elif grid[i][k] == "1" and (i,k) not in visited:
                    count +=1 
                    search_queue = deque()
                    search_queue.append((i,k))
                    visited.add((i , k))
                    while search_queue:
                        r , c = search_queue.popleft()
                        lists = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
                        for nr , nc in lists:
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1" and (nr, nc) not in visited:
                                visited.add((nr , nc))
                                search_queue.append((nr,nc))

        return count
        