class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s)//2
        a = s[:half]
        b = s[half:]
        vowels = ['a', 'e', 'i', 'o', 'u']
        def countVowels(st):
            vowels = 'AaIiEeOoUu'
            count = len([each for each in st if each in vowels])
            return count
        resA = countVowels(a)
        resB = countVowels(b)
        if resA == resB:
            return True
        else:
            return False