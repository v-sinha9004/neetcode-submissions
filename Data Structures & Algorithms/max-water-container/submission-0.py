class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n - 1

        res = 0

        while i < j:
            area = min(heights[i], heights[j]) * (j-i)

            res = max(area, res)

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        
        return res