class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0 
        j = 0
        res = 0
        n = len(s)

        count = defaultdict(int)

        while j < n:
            count[s[j]] += 1
            
            while count[s[j]] > 1:
                count[s[i]] -= 1
                i += 1

            res = max(res, j - i + 1)
            j += 1

        return res
