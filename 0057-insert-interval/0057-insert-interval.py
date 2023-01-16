class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
            leftIndex = bisect.bisect_left(intervals, newInterval)
            intervals.insert(leftIndex, newInterval)
            result = []
            for interval in intervals:
                if result and result[-1][1] >= interval[0]:
                    result[-1][0] = min(result[-1][0], interval[0])
                    result[-1][1] = max(result[-1][1], interval[1])
                else:
                    result.append(interval)
            return result