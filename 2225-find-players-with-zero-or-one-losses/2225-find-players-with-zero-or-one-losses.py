class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers, count = [], [], {}
        for winner,loser in matches:
            count[winner] = count.get(winner,0)
            count[loser] = count.get(loser,0)+1
        for player, loss in count.items():
            if loss == 0:
                winners.append(player)
            if loss== 1:
                losers.append(player)
        return [sorted(winners), sorted(losers)]