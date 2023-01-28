class SummaryRanges:
    def __init__(self):
        self.intervals = []
    
    def merge(self, idx):
        if idx+1 < len(self.intervals) and idx>=0 and self.intervals[idx+1][0]-self.intervals[idx][1]<=1:
            self.intervals[idx][1] = max(self.intervals[idx][1], self.intervals[idx+1][1])
            self.intervals.pop(idx+1)        

    def addNum(self, val: int) -> None:
        l, r = 0, len(self.intervals)-1
        while l<=r:
            mid = (l+r)//2
            if self.intervals[mid][0] >= val:
                r = mid - 1
            else:
                l = mid + 1

        self.intervals.insert(l, [val, val])
        self.merge(l)
        self.merge(l-1)
        
    def getIntervals(self) -> List[List[int]]:
        return self.intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()