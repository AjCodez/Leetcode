class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # usl=[]
        # for z in words1:
        #     f=0
        #     for j in words2:
        #         i=z
        #         for k in j:
        #             y=i
        #             if k not in y:
        #                 f=-1
        #                 break
        #             else:
        #                 i=i.replace(k,'',1)
        #         if f==-1:
        #             break
        #         else:
        #             f+=1
        #     if f==len(words2):
        #         usl.append(z)
        # return usl
        # usl=[]
        # for i in words1:
        #     for j in words2:
        #         f=0
        #         k=set(j)
        #         for l in k:
        #             if i.count(l)<j.count(l):
        #                 f=-1
        #                 break
        #         if f==-1:
        #             break
        #     else:
        #         usl.append(i)
        # return usl
        target = {}
        for targetWord in words2:
            toAdd = {}
            for letter in targetWord:
                if letter not in toAdd:
                    toAdd[letter] = 1
                else:
                    toAdd[letter] += 1
            
            for letter, occur in toAdd.items():
                if letter in target:
                    target[letter] = max(occur, target[letter])
                else:
                    target[letter] = occur
        
        ret = []
        for a in words1:
            toInclude = True
            for key in target:
                if a.count(key) < target[key]:
                    toInclude = False
                    break
            if toInclude:
                ret.append(a)
        return ret