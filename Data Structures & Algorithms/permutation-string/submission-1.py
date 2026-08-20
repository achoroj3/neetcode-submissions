class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        f1 = [0] * 26
        f2 = [0] * 26
        k = len(s1)
        for ch in s1:
            f1[ord(ch) - 97] += 1
        for i in range(k):
            f2[ord(s2[i]) - 97] += 1
        if f1 == f2:
            return True
        for i in range(k, len(s2)):
            f2[ord(s2[i]) - 97]+= 1
            f2[ord(s2[i-k]) - 97]-= 1
            if f1 == f2:
                return True
        return False


