#User function Template for python3



def maxArea(A,le):
    
    i, j = 0, le-1
    ans = 0
    while i < j:
        ans = max(ans, (j-i)*min(A[i], A[j]))
        if A[j] < A[i]:
            j -= 1
        else:
            i += 1
    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    l = list(map(int,input().split()))
    
    print(maxArea(l,n))
    
    
# } Driver Code Ends