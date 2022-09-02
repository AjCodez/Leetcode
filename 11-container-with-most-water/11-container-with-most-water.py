class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        w=0
        while l<r:
            w=max(w,(r-l)*min(height[r],height[l]))
            if height[r]<height[l]:
                r-=1
            else:
                l+=1
        return w