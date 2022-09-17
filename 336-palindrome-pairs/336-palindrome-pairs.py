class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # l=[]
        # for i in range(len(words)):
        #     for j in range(len(words)):
        #         if i!=j:
        #             a=words[i]+words[j]
        #             if a==a[::-1]:
        #                 l.append([i,j])
        # return l
#         
#         wordict = {}
#         res = [] 
#         for i in range(len(words)):
#             wordict[words[i]] = i
#         for i in range(len(words)):
#             for j in range(len(words[i])+1):
#                 tmp1 = words[i][:j]
#                 tmp2 = words[i][j:]
#                 if tmp1[::-1] in wordict and wordict[tmp1[::-1]]!=i and tmp2 == tmp2[::-1]:
#                     res.append([i,wordict[tmp1[::-1]]])
#                 if j!=0 and tmp2[::-1] in wordict and wordict[tmp2[::-1]]!=i and tmp1 == tmp1[::-1]:
#                     res.append([wordict[tmp2[::-1]],i])

#         return res

        new_words = []
        for i, word in enumerate(words):
            new_words.append((word, 1, i))
            new_words.append((word[::-1], 0, i))
        
        new_words.sort()
        n = len(new_words)
        output = []
        for i in range(n):
            word_1, bool_1, idx1 = new_words[i]
            for j in range(i+1, n):
                word_2, bool_2, idx2 = new_words[j]
                if word_2.startswith(word_1):
                    if bool_1 != bool_2 and idx1 != idx2:
                        rest = word_2[len(word_1):]
                        if rest == rest[::-1]:
                            if bool_1:
                                output.append([idx1, idx2])
                            else:
                                output.append([idx2, idx1])
                else:
                    break # not possible
        return output