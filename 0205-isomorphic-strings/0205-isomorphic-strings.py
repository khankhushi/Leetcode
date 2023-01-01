class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t = dict()
        if len(s) != len(t):
            return False
        if len(set(s)) != len(set(t)):
            return False
        for i in range(len(s)):
            if s[i] not in s_t:
                s_t[s[i]] = t[i]
            elif s_t[s[i]] != t[i]:
                return False
        return True
        