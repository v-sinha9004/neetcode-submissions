class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}

        for i, n in enumerate(nums):
            temp[n] = i

        # single scan
        for i, n in enumerate(nums):
            diff = target - nums[i]

            if diff in temp and temp[diff] != i:
                return [i, temp[diff]]

        
        return []