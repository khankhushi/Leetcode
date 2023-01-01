class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strings = s.split(" ")
        str_pattern = dict()
        if len(strings) != len(pattern):
            return False
        if len(set(strings)) != len(set(pattern)):
            return False
        
        for i in range(len(strings)):
            if strings[i] not in str_pattern:
                str_pattern[strings[i]] = pattern[i]
            elif str_pattern[strings[i]] != pattern[i]:
                return False
        return True
        
    
        
        