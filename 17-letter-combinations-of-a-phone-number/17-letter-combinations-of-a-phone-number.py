class Solution:
    def letterCombinations(self, d: str) -> List[str]:
        c = {'2':'abc',
                '3':'def', 
                '4': 'ghi', 
                '5':'jkl',
                '6':'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'
               }
        l=[]
        if len(d)==1:
            for i in c[d]:
                l.append(i)
        elif len(d)==2:
            for i in c[d[0]]:
                for j in c[d[1]]:
                    l.append(i+j)
        elif len(d)==3:
            for i in c[d[0]]:
                for j in c[d[1]]:
                    for k in c[d[2]]:
                        l.append(i+j+k)
        elif len(d)==4:
            for i in c[d[0]]:
                for j in c[d[1]]:
                    for k in c[d[2]]:
                        for a in c[d[3]]:
                            l.append(i+j+k+a)
        return l