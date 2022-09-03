class Solution:
    def rec(self,num,n,k,arr):
        if n==0:
            arr.append(num)
            return
        for i in range(10):
            if abs((num%10)-i)==k:
                self.rec((num*10)+i,n-1,k,arr)
        return
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # if k==9:
        #     a=''
        #     ar=[]
        #     for i in range(n):
        #         if i%2==0:
        #             a+='9'
        #         else:
        #             a+='0'
        #     if a:
        #         ar.append(a)
        #     return ar
        # if k==0:
        #     a=''
        #     ar=[]
        #     for i in range(1,10):
        #         a=str(i)*n
        #         ar.append(a)
        #     return ar
        arr=[]
        for i in range(1,10):
            self.rec(i,n-1,k,arr)
        return arr