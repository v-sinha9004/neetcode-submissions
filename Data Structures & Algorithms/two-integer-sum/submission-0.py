class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array_2d = []
        for i, n in enumerate(nums):
            array_2d.append([n, i])

        i, j = 0, len(nums) - 1

        array_2d.sort()
        while i < j:
            total = array_2d[i][0] + array_2d[j][0]

            if total == target:
                return [
                        min(array_2d[i][1], array_2d[j][1]),
                        max(array_2d[i][1], array_2d[j][1])
                    ]
            elif total < target:
                i += 1
            else:
                j -= 1
        
        return []