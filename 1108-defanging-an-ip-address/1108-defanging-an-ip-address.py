class Solution:
    def defangIPaddr(self, add: str) -> str:
        defangIp = []
        for i in range(len(add)):
            if add[i] == '.':
               defangIp.append('[.]')
            else:
                defangIp.append(add[i])
        return ''.join(defangIp)
        