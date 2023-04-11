class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for chara in s:
            if chara == '*':
                stack.pop()
            else:
                stack.append(chara)
        return "".join(stack)