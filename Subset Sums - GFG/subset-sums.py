#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		l=[]
		
		def ss(a,i):
		  #  if i==N:
		  #      return
		    if i==N:
		        l.append(sum(a)) if a else l.append(0)
		        return
		    a.append(arr[i])
		    ss(a,i+1)
		    a.pop()
		    ss(a,i+1)
		 
	    arr.sort()
	    ss([],0)
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