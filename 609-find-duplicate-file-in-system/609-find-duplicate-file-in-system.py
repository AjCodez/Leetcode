class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        l=[]
        
        for i in paths:
            a=i.split()
            
            for j in range(1,len(a)):
                b=a[j].split('(')
                c=b[1][:len(b[1])-1]
                d[c].append(a[0]+'/'+b[0])
                    
        for i in d:
            if len(d[i])>1:
                l.append(d[i])
                
        return l