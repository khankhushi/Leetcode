class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succp: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append([b, succp[i]])
            graph[b].append([a, succp[i]])
            
        max_prob = [0.0] * n    
        max_prob[start] = 1.0
        
        queue = deque([start])
        while queue:
            curr_node = queue.popleft()
            for nxt_node, path_prob in graph[curr_node]:

                
                if max_prob[curr_node] * path_prob > max_prob[nxt_node]:
                    max_prob[nxt_node] = max_prob[curr_node] * path_prob
                    queue.append(nxt_node)
                    
        return max_prob[end]