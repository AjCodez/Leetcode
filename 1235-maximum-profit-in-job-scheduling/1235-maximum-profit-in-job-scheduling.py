class Solution:
    def fun(self,arr,i,memo):
        if(i==len(arr)):
            return 0
        if i in memo:
            return memo[i]
        a=self.fun(arr,i+1,memo)
        bj=-1
        for j in range(i+1,len(arr)):
            if(arr[j][0]>=arr[i][1]):
                bj=j
                break
        if(bj==-1):
            b=arr[i][2]
        else:
            b=arr[i][2]+self.fun(arr,bj,memo)
        memo[i]=max(a,b)
        return max(a,b)
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        arr=[]
        for i in range(len(startTime)):
            arr.append([startTime[i],endTime[i],profit[i]])
        arr.sort(key=lambda x:x[0])
        return self.fun(arr,0,{})