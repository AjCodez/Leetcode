class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        return len(seen := sum(([(d,i),(j,d),(d,i//3,j//3)] if  d != "." else [] for i, row in enumerate(board) for j, d   in enumerate(row)),[])) == len(set(seen))