class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return nums[0]
        sum = 0
        fsum = float("-inf")
        for i in nums :
            sum += i 
            if sum > fsum :
                fsum = sum
            if sum < 0 :
                sum = 0



            
        return fsum
