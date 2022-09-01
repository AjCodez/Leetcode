class Solution:
    def minimumSum(self, num: int) -> int:
        n=sorted(str(num))
        n1=''
        n2=''
        for i in range(len(n)):
            if i%2==0:
                n1+=n[i]
            else:
                n2+=n[i]
        return int(n1)+int(n2)