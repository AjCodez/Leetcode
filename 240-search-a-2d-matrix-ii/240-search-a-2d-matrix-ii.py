class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        if target<matrix[0][0] or target>matrix[m-1][n-1]:
            return False
        t1,t2=0,0
        for i in range(max(m,n)):
            if i<n:
                if matrix[0][i]<=target:
                    b=i
                else:
                    t1=1
            if i<m:
                if matrix[i][0]<=target:
                    a=i
                else:
                    t2=1
            if t1>0 and t2>0:
                break
        for i in range(a+1):
            l=matrix[i]
            low=0
            mid=0
            high=b

            while low<=high:
                mid=(high+low)//2
                if l[mid]<target:
                    low=mid+1
                elif l[mid]>target:
                    high=mid-1
                else:
                    return True
        else:
            return False