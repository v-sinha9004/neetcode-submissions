class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p, s = [0] * n, [0] * n

        p[0] = 1
        s[n-1] = 1

        for i in range(1, n):
            p[i] = p[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            s[i] = s[i+1] * nums[i+1]

        res = []

        for i in range(n):
            res.append(p[i] * s[i])

        return res