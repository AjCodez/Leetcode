class Solution:
    def trav(self, grid, i , j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return 
        if grid[i][j]=='0':
            return
        grid[i][j]='0'
        self.trav(grid,i-1,j)
        self.trav(grid,i,j-1)
        self.trav(grid,i+1,j)
        self.trav(grid,i,j+1)
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    self.trav(grid,i,j)
                    count+=1
        return count