class Solution:
    def climbStairs(self, n: int) -> int:
        steps = {}
        def helper(n):
            if n ==1 :
                return 1
            if n == 2 : 
                return 2
            if n in steps :
                return steps[n]
            else:
                steps[n] = helper(n-1) + helper(n-2)
                return steps[n]
        return helper(n)