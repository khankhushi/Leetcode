import collections

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cont = Counter(arr)
        freq = sorted(cont.values(), reverse=True)
        half, size = len(arr)/2,0
        while half>0:
            half -= freq[size]
            size+= 1
            
            
            
        
        
        
        # arr.sort()
        # for i in range(len(arr)):
        #     for j in range(i+1,len(arr)-1):
        #         if arr[i]== arr[j]:
        #             arr.pop(i)
        #             arr.pop(j)
        #     new_li.append(arr[i])
        return size
        
        