class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(len(matrix)//2):
            for j in range(len(matrix)):
                matrix[j][i],matrix[j][len(matrix)-i-1]=matrix[j][len(matrix)-i-1],matrix[j][i]