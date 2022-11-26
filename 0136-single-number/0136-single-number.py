class Solution:
    def singleNumber(self, arr: List[int]) -> int:
        arr.sort()
        extra = []
        for i in range(len(arr)):
            if len(arr) == 1:
                return arr[0]
            if arr[i] not in extra:
                extra.append(arr[i])
            else:
                extra.pop()
        return extra[0]

