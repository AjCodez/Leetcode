class Solution:
    def trap(self, height: List[int]) -> int:
        l=[]
        r=[0]*len(height)
        
        c=0
        
        for i in height:
            c=max(c,i)
            l.append(c)
        c=0
        for i in range(len(height)-1,-1,-1):
            c=max(c,height[i])
            r[i]=c
            
        c=0
        for i in range(len(height)):
            c+=min(l[i],r[i])-height[i]
        
        return c