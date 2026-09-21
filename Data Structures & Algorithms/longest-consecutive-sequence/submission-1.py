class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)
        res = 0

        for a in arr:
            if (a - 1) in arr:
                continue

            length = 1

            while (a + 1) in arr:
                a += 1
                length += 1
            
            res = max(length, res)

        
        return res