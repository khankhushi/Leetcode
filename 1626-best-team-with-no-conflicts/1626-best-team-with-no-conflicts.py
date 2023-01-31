class Solution:

    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        d = [(ages[i],scores[i]) for i in range(len(ages))]
        l = sorted(d, key=lambda x:(x[0],x[1]))
        dp = [0 for i in range(len(scores))]
        dp[0] = l[0][1]
        for i in range(1,len(scores)):
            dp[i] = l[i][1]
            for j in range(i):
                if l[j][1]<=l[i][1]:
                    dp[i] = max(dp[i],l[i][1]+dp[j])
        return max(dp)