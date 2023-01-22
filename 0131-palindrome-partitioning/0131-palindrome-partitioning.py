class Solution:
    def partition(self, ss):
        if len(ss) == 0: return [[]]
        ans = []
        
        def H(L,S):
            #print(ans,L,S)
            if len(S) == 0:
                ans.append(L)
                return
                
            for i in range(1, len(S)+1):
                s = S[:i]
                #print(i, s, S)
                if s == s[::-1]: H(L+[s], S[i:])
				
        H([], ss)
        return ans