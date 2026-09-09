class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = defaultdict(int)

        for num in nums:
            temp[num] += 1

        heap = []
        
        for num, cnt in temp.items():
            heapq.heappush(heap, ([cnt, num]))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res