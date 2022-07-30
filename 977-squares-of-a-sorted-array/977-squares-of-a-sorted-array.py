class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqr = []
        sqr_num = 0
        for i in range(len(nums)):
            sqr_num = pow(nums[i], 2)
            sqr.append(sqr_num)
        sqr.sort(reverse=False)   
        return sqr
        