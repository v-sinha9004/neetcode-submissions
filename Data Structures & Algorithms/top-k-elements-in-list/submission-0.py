class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = defaultdict(int)

        for num in nums:
            temp[num] += 1

        arr = []
        for val, cnt in temp.items():
            arr.append([cnt, val])
        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])

        return res 