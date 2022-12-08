class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # return nums[len(nums)//2]
        
        # ele, count = nums[0], 0
        #     for element in nums:
        #         if element == ele:
        #                 count+=1
        #         elif count ==0:
        #             ele, count = element, 1
        #         else:
        #             count-=1
        #     return ele
        
        dic = {}
        for ele in nums:
            dic[ele] = dic.get(ele, 0) + 1
            if dic[ele] > len(nums)//2:
                return ele