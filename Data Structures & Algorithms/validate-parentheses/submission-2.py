class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            '{': '}',
            '[': ']',
            '(': ')'
        }

        stack = []

        for i in s:
            if i in '{[(':
                stack.append(i)
            else:
                if not stack or mp[stack.pop()] != i:
                    return False

        return len(stack) == 0