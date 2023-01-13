class Solution:
    def countPoints(self, s: str) -> int:
        f = []
        for j in range(0,10):
            f.append(set())
        print(f)
        
        for i in range(0, len(s), 2):
            colour = s[i]
            number = int(s[i+1])
            f[number].add(colour)
        print(f)
        
        return sum(1 for x in f if len(x)==3)
            
                