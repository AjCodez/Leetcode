from heapq import *
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        if n==1:
            return speed[0]*efficiency[0]
        h=[]
        for i in range(n):
            heappush(h,(-efficiency[i],speed[i]))
        th=[]
        s=0
        e=0
        ans=s*e
        for i in range(n):
            if len(th)<k:
                t=heappop(h)
                s+=t[1]
                e=-t[0]
                heappush(th,t[1])
                ans=max(ans,s*e)
                continue
            t=heappop(h)
            s+=t[1]
            e=-t[0]
            t2=heappushpop(th,t[1])
            s-=t2
            ans=max(ans,s*e)
        return ans%((10**9)+7)