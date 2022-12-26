class Solution:
    def fib(self, n: int) -> int:
        # if n == 0:
        #     return 0
        # elif n == 1:
        #     return 1
        # else:
        #     return (fib(n-1)+fib(n-2))
        a, b = 0, 1
        for _ in repeat(None, n):
            a, b = b, a+b
        return a
        