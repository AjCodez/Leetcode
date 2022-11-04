class Solution:
    def reverseVowels(self, s: str) -> str:
        v={'a','A','e','E','i','I','o','O','u','U'}
        l=[]
        s=list(s)
        for i in s:
            if i in v:
                l.append(i)
        p=-1
        for i in range(len(s)):
            if s[i] in v:
                s[i]=l[p]
                p-=1
        return ''.join(s)