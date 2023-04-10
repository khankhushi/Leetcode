class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        dic = {')':'(', ']':'[', '}':'{'}
        for i in range(len(s)):
            if not st:
                st.append(s[i])
            elif s[i] not in dic:
                st.append(s[i])
            elif s[i] in dic and st[-1] == dic[s[i]]:
                st.pop()
            else:
                return False
        return not st
        