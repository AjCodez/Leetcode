#User function Template for python3

class Solution:
	def NthTerm(self, n):
		a=2
		for i in range(2,n+1):
		    a=a*i+1
		return a%(10**9+7)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.NthTerm(n)
		print(ans)

# } Driver Code Ends