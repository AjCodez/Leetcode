class Solution:
    def countAsterisks(self, s: str) -> int:
        ss = s.split("|")
        a=0
        for i in range(0,len(ss),2):
            for j in ss[i]:
                if j=='*':
                    a+=1
        return a