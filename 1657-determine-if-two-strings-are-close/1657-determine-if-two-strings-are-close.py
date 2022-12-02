class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        l1 = len(word1)
        l2 = len(word2)
        
        if l1 != l2: return 0
        
        unique1 = Counter(word1)
        unique2 = Counter(word2)
        
        for i in unique1.keys():
            if i not in unique2.keys():
                return 0
        fre1 = Counter(unique1.values())
        fre2 = Counter(unique2.values())
        
        for f, v in fre1.items():
            if fre2[f] != v:
                return 0
        return 1