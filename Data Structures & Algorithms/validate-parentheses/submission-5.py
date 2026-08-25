class Solution:
    def isValid(self, s: str) -> bool:
        opening = []
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                opening.append(s[i])
            else:
                if len(opening) == 0 or s[i] == ')' and opening[-1] != '(':
                    return False
                if len(opening) == 0 or s[i] == ']' and opening[-1] != '[':
                    return False
                if len(opening) == 0 or s[i] == '}' and opening[-1] != '{':
                    return False
                if opening:
                    opening.pop()
        if opening:
            return False
        return True
                