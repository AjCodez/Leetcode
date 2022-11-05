#User function Template for python3

class Solution:
    def minPartition(self, N):
        c=[1,2,5,10,20,50,100,200,500,2000]
        l=[]
        def curr(amt,i):
            if amt==0:
                return
            if c[i]<=amt:
                l.append(c[i])
                curr(amt-c[i],i)
            else:
                curr(amt,i-1)
            return
        curr(N,9)
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends