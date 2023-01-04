class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        # tasks.sort()
        cnt = Counter(tasks)
        minm = 0
        # for i in range(len(tasks)):
        #     if tasks.count(tasks[i]) not in cnt:
        #         cnt.append(tasks.count(tasks[i]))
        
        for i in cnt:
            countt = cnt[i]
            if countt == 1:
                return -1 
            if countt% 3 == 0:
                minm += countt//3 
            else:
                minm += countt//3 + 1
        return minm
                
          