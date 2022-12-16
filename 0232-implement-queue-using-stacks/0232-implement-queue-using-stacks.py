#???
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)
        

    def pop(self) -> int:
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())
        res = self.s2.pop()
    
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())
        return res

    def peek(self) -> int:
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())
        res = self.s2[len(self.s2) - 1]

        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())
        return res
        

    def empty(self) -> bool:
        return len(self.s1) == 0