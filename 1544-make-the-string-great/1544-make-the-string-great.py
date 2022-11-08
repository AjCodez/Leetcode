class Solution:
    def makeGood(self, s: str) -> str:
        
        ss=[]
        
        for i in s:
            
            if not ss:
                ss.append(i)
                
            elif (i.islower() and ss[-1].isupper() and i.upper()==ss[-1]) or (ss[-1].islower() and i.isupper() and ss[-1].upper()==i):
                ss.pop()
                
            else:
                ss.append(i)
                
        return "".join(ss)