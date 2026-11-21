class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x , y in points :
            dist = x**2 + y**2 
            point = [x , y]
            heapq.heappush(heap,(dist , point))
        result = []
        while k>0 :
            dist , point = heapq.heappop(heap)
            result.append(point)
            k-=1
        return result