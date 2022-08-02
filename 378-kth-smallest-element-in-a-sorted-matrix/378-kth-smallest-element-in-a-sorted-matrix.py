class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        length = len(matrix)
        l=[]
        for i in range(length):
            for j in range(length):
                l.append(matrix[i][j])
        return sorted(l)[k-1]