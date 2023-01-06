class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in "+-/*":
                stack.append(t)
            else:
                right,left = float(stack.pop()), float(stack.pop())
                if t == "+":
                    stack.append(left+right)
                elif t == "-":
                    stack.append(left-right)
                elif t == "*":
                    stack.append(left*right)
                else:
                    stack.append(float(int(left/right)))
        return int(stack.pop())
                
