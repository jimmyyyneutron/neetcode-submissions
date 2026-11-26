class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 :
            return 1
        prev = 1
        cur = 2
        for i in range(3, n+1):
            new = prev + cur 
            prev = cur 
            cur = new
        return cur