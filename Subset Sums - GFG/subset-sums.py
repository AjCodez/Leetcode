#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		l=[]
		
		def ss(i,s):
		    if i==N:
		        l.append(s)
		        return
		    ss(i+1,s+arr[i])
		    ss(i+1,s)
		 
	    ss(0,0)
	    return l
	    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends