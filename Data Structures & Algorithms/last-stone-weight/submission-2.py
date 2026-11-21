class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        greatest = [-x for x in stones]
        heapq.heapify(greatest)
        while len(greatest) > 1 :
            first = -heapq.heappop(greatest)
            second= -heapq.heappop(greatest)
            if first != second :
                if first < second :
                    first = 0
                    second = second - first 
                    heapq.heappush(greatest , -second)
                elif first > second :
                    first = first - second
                    second = 0
                    heapq.heappush(greatest , -first)
            if not greatest :
                return 0
        return -greatest[0]