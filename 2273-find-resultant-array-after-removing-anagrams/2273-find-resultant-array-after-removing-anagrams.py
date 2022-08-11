class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        dp1=[]
        dp2=[]
        for i in words:
            s=''
            word=sorted(set(i))
            for j in word:
                s+=j+str(i.count(j))
            if s not in dp1:
                dp1=[s]
                dp2.append(i)
            
        return dp2