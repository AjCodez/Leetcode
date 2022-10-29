class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        l=[]
        for i in range(len(plantTime)):
            l.append([plantTime[i],growTime[i]])
        l.sort(key=lambda x:x[1],reverse=True)
        # print(l)
        
        ans=0
        f=0
        for i in range(len(l)):
            f+=l[i][0]
            ans=max(ans,f+l[i][1])
        
        return ans