class Solution:
    def romanToInt(self, s: str) -> int:
        l = {'I':1,'V':5,'IV':4,'X':10,'IX':9,'L':50,'C':100,'D':500,'M':1000,'XL':40,'XC':90,'CD':400,'CM':900}
        n=0
        i=0
        while i!=len(s):
            try:
                if s[i]+s[i+1] in l:
                    n+=l[s[i]+s[i+1]]
                    i+=2
                else:
                    n+=l[s[i]]
                    i+=1
            except:
                n+=l[s[i]]
                i+=1
        return n