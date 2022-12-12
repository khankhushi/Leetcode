#??
class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return 1
#         dic = [-1 for i in range(n)]
#         dic[0], dic[1] = 1, 2
#         return self.helper(n-1, dic)

#     def helper(self, n, dic):
#         if dic[n] < 0:
#             dic[n] = self.helper(n-1, dic)+self.helper(n-2, dic)
#         return dic[n]

    def __init__(self):
        self.dic = {1:1, 2:2}

    def climbStairs(self, n):
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]

