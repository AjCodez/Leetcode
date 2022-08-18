class Solution:
    def thousandSeparator(self, n: int) -> str:
        n=str(n)
        s=''
        c=0
        for i in range(len(n)-1,-1,-1):
            s=n[i]+s
            c+=1
            if c%3==0 and c!=len(n):
                s='.'+s
        return s