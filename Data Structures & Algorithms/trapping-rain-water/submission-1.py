class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = {}
        suffix = {}
        n = len(height)

        l_max = 0
        for i, h in enumerate(height):
            l_max = max(l_max, h)
            prefix[i] = l_max

        r_max = 0
        for j in range(n - 1, -1, -1):
            r_max = max(r_max, height[j])
            suffix[j] = r_max

        res = 0
        for i, h in enumerate(height):
            rain = min(prefix[i], suffix[i]) - h
            res += rain

        return res
