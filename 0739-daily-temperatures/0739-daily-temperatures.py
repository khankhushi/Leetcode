#???
class Solution:
    def dailyTemperatures(self, T):
        ans, s = [0]*len(T), deque()
        for cur, cur_temp in enumerate(T):
            while s and cur_temp > T[s[-1]]:
                ans[s[-1]] = cur - s[-1]
                s.pop()
            s.append(cur)
        return ans