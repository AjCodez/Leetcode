#User function Template for python3


import bisect
class Solution:

	def removals(self,arr, n, k):
		arr.sort()
		ans=n
		for r in range(n):
            ans=min(n-bisect.bisect_right(arr,arr[r]+k)+r,ans)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.removals(arr, n, k)
        print(ans)
        tc -= 1
# } Driver Code Ends