class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res=0
        cur=0
        lookup=collections.Counter()
        lookup[0]=1
        
        for i in nums:
            cur+=i
            cur%=k
            res+=lookup[cur]
            lookup[cur]+=1
        print(lookup)
        return res