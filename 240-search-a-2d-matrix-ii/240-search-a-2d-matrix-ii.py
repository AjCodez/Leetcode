class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        if target<matrix[0][0] or target>matrix[m-1][n-1]:
            return False
        a,b=0,0
        for i in range(m):
            if matrix[i][0]<=target:
                a+=1
            else:
                break
        for i in range(n):
            if matrix[0][i]<=target:
                b+=1
            else:
                break
        for i in range(a):
            l=matrix[i]
            low=0
            mid=0
            high=b-1

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