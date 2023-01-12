#??
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [0] * n
        tree = collections.defaultdict(list)
        for a, b in edges:                             
            tree[a].append(b)
            tree[b].append(a)
        def dfs(node):                                 
            nonlocal visited, ans, tree
            c = collections.Counter(labels[node])
            for neither in tree[node]:
                if neither in visited: continue            
                visited.add(neither)
                c += dfs(neither)                          
            ans[node] = c.get(labels[node])           
            return c
        visited = set([0])
        dfs(0)
        return ans