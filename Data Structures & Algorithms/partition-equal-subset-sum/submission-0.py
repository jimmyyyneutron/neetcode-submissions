class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 :
            return False
        dp =set()
        dp.add(0)
        target = sum(nums) // 2
        for i in nums :
            temp = set()
            for k in dp :
                temp.add(k)
                temp.add(k+i)
            dp=temp
        return target in dp