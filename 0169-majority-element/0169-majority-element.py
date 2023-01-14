class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = Counter(nums).most_common(1)[0][0]
        
        return n