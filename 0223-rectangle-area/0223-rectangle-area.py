class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        l1=abs(by2-by1)
        b1=abs(bx2-bx1)
        l2=abs(ay2-ay1)
        b2=abs(ax2-ax1)
        
        area = (l1*b1)+(l2*b2)
#         # return area
#         f=False
#         if ((ax1>=bx1 and ax1<=bx2) or (ax2<=bx1 and ax2>=bx2)) and ((bx1>=ax1 and bx1<=ax2) or (bx1<=ax1 and bx1>=ax2)):
#             f=True
#         if f and (((ay1>=by1 and ay1<=by2) or (ay2<=by1 and ay2>=by2)) and ((by1>=ay1 and by1<=ay2) or (by1<=ay1 and by1>=ay2))):
#             f=True
#         else:
#             f=False
            
#         if not f:
#             return area
        x1=max(ax1,bx1)
        x2=min(ax2,bx2)
        y1=max(ay1,by1)
        y2=min(ay2,by2)
        inter = (x1-x2)*(y1-y2)
        if x2-x1<0 or y2-y1<0:
            inter=0
        return area-inter