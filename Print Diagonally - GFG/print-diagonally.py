#User function Template for python3

def downwardDigonal(N, A): 
    # code here 
    l=[]
    for i in range(N):
        j=i
        k=0
        while j>=0 and i<N:
            l.append(A[k][j])
            k+=1
            j-=1
    for i in range(1,N):
        j=N-1
        k=i
        while k<=N-1 and j>-1:
            l.append(A[k][j])
            k+=1
            j-=1
    return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix =[]
        for i in range(n):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
        ans = downwardDigonal(n,matrix)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends