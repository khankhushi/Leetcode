class RandomizedSet:

    def __init__(self):
        self.dataMap = {}
        self.data = []

    def insert(self, val: int) -> bool:
        
        if val in self.dataMap: #Vhecking in dictionary to comply to time complexity
            return False
        self.dataMap [val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not val in self.dataMap: #Vhecking in dictionary to comply to time complexity
            return False
        last_elem = self.data[-1]
        index_elem_remove = self.dataMap[val]
        
        self.dataMap[last_elem] = index_elem_remove
        self.data[index_elem_remove] = last_elem
        
        self.data[-1] = val
        self.data.pop()
        self.dataMap.pop(val)
        
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()