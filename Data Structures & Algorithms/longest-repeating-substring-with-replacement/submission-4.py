class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for c in charSet:
            l = 0 
            count = 0

            for i in range(len(s)):
                if s[i] == c:
                    count += 1

                while (i - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    
                    l += 1
                
                res = max(res, i - l + 1)

        return res
