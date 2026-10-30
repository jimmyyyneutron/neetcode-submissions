class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        k = max(piles)
        while low <= high :
            mid = (low + high) // 2
            hours = 0 
            for i in piles:
                hours += math.ceil(i/mid) 
            if hours <= h :
                high = mid -1 
                k = mid 
            else:
                low = mid +1 
        return k
        