class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr = []
        
        for i in range(len(names)):
            arr.append([heights[i], names[i]])
        arr = sorted(arr, reverse=True)
        return (names for heights, names in arr)
            