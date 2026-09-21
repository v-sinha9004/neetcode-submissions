class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = defaultdict(int)
        n = len(nums)
        res = set()

        for num in nums:
            count[num] += 1
        
        for i, ni in enumerate(nums):
            count[ni] -= 1

            if i and ni == nums[i-1]:
                continue

            for j in range(i+1, n):
                count[nums[j]] -= 1

                if j - 1 > i and nums[j] == nums[j-1]:
                    continue

                target = -(nums[i] + nums[j])

                if count[target] > 0:
                    res.add(tuple([nums[i], nums[j], target]))

            for j in range(i+1, n):
                count[nums[j]] += 1

        return [list(a) for a in res]
                

