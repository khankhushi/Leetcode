class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for i in range(len(operations)):
            if operations[i][0] == "+" or operations[i][1]== "+":
                x+= 1
            else:
                x-=1
        return x
        