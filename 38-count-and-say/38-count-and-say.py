class Solution:
    def countAndSay(self, n: int) -> str:
        i=1
        s='1'
        while i<n:
            ss=''
            c=0
            cs=''
            for j in s:
                if j==cs:
                    c+=1
                else:
                    if cs:
                        ss+=str(c)+cs
                    cs=j
                    c=1
            if cs:
                ss+=str(c)+cs
            s=ss
            i+=1
        return s