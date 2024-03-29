class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if(len(points)<=2):
            return len(points)
        def findSlope(p1,p2):
            x1,y1=p1
            x2,y2=p2
            if x1-x2==0:
                return inf
            return(y1-y2)/(x1-x2)
        res=1
        for i,p1 in enumerate(points):
            slopes=defaultdict(int)
            for p2 in points[i+1:]:
                slope=findSlope(p1,p2)
                slopes[slope]+=1
                res=max(slopes[slope],res)
        return res+1