class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        grid = [float("inf")] * (amount + 1)
        grid[0] = 0
        for i in range(1, amount + 1):
            for k in coins :
                if k > i :
                    continue
                grid[i] = min(grid[i-k] + 1, grid[i]) 
        if grid[-1] != float("inf") :
            return grid[-1]
        else : 
            return -1

        