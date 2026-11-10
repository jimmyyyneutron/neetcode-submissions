class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums) 
        longest = 0
        for i in nums_set :
            if not i -1 in nums_set:
                current = i
                sequence = 1
                while current + 1 in nums_set:
                    sequence += 1
                    current += 1
                longest = max(longest, sequence)
        return longest
        
