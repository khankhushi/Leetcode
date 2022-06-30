class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        nums=str(num)
        count=0
        for i in range(k,len(nums)+1):
            sub_string=int(nums[i-k:i])
            if sub_string!=0 and num%sub_string==0:
                count+=1
        return count