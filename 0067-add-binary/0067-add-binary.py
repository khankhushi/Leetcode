class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimalq = int(a,2)
        decimalb = int(b,2)
        sum= decimalq+decimalb
        s = format(sum, 'b')
        return s
        
        