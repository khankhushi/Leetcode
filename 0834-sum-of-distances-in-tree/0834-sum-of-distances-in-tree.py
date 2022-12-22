#????
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        cnt=[0]*n
        dic=defaultdict(list)
        for x,y in edges:
            dic[x].append(y)
            dic[y].append(x)

        vis=[True]*n
        ret=[0]*n
        def count(x=0,lev=0):
            ret[0]+=lev
            tmp=0
            cnt[x]=1
            vis[x]=False
            for nxt in dic[x]:
                if vis[nxt]:
                    tmp+=1+count(nxt,lev+1)
            cnt[x]=tmp
            return tmp
        count()

        st=deque([0])
        vis=[True]*n
        vis[0]=False
        while st:
            sn=len(st)
            for _ in range(sn):
                cur=st.popleft()
                for nxt in dic[cur]:
                    if vis[nxt]:
                        ret[nxt]=(ret[cur]-cnt[nxt]-1)+(n-cnt[nxt]-1)
                        st.append(nxt)
                        vis[nxt]=False
        return ret
                
        