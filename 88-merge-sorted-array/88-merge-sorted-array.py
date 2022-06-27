class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new_nums1 = nums1[:m]  
               
        t1 = 0
        t2 = 0
               
        for t in range(n + m):
      
            if t2 >= n or (t1 < m and new_nums1[t1] <= nums2[t2]):
                nums1[t] = new_nums1[t1] 
                t1 += 1
            else:
                nums1[t] = nums2[t2]
                t2 += 1
        