class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ss=['']*numRows
        i=0
        f=0
        while True:
            if f==1:
                break
            for j in range(numRows):
                ss[j]+=s[i]
                i+=1
                if i==len(s):
                    f=1
                    break
            if f==1:
                break
            for j in range(numRows-2,0,-1):
                ss[j]+=s[i]
                i+=1
                if i==len(s):
                    f=1
                    break
            if f==1:
                break
        return ''.join(ss)