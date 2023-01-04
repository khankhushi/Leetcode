class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt = Counter(tasks)
        minm = 0
        for i in cnt:
            countt = cnt[i]
            if countt == 1:
                return -1 
            if countt% 3 == 0:
                minm += countt//3 
            else:
                minm += countt//3 + 1
        return minm
                
          