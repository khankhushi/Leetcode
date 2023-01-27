class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        S = set(words)
        ans = []
        for word in words:
            if not word: 
                continue
            stack = [0]
            seen = {0}
            M = len(word)
            while stack:
                node = stack.pop()
                if node == M:
                     ans.append(word)
                     break
                for j in range(1, M - node + 1):
                     if word[node:node+j] in S and node + j not in seen \
                         and not (node==0 and node+j==M): 
                         stack.append(node + j)
                         seen.add(node + j)
        return ans