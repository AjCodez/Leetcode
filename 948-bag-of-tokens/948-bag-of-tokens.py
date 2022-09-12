class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if not len(tokens):
            return 0
        tokens.sort()
        p1=0
        p2=len(tokens)-1
        s=0
        score=0
        if power<tokens[p1] and score==0:
            return 0
        while p1<=p2:
            if power>=tokens[p1]:
                score+=1
                s=max(s,score)
                power-=tokens[p1]
                p1+=1
            elif score>0:
                score-=1
                power+=tokens[p2]
                p2-=1
        s=max(s,score)
        return s