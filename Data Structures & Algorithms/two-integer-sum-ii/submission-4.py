class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # binary search
        n = len(numbers)

        for i, num in enumerate(numbers):
            b_find = target - num

            # start binary search
            start = i + 1
            end = n - 1

            while start <= end:
                mid = (start + end) // 2
                if numbers[mid] == b_find:
                    return [i + 1, mid + 1]
                elif numbers[mid] < b_find:
                    start = mid + 1
                else:
                    end = mid - 1