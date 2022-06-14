class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        def isvalid(x):
            #print(x)
            temp=[i for i in x if i!="."]
            return len(temp)==len(set(temp))
        
        def rowvalid(board):
            for r in board:
                if isvalid(r)==False: return False
            return True
        
        def colvalid(board):
            for c in zip(*board):
                if isvalid(c)==False: return False
            return True
        
        
        def squaresvalid(bs):
            for b in bs:
                if isvalid(b[0])==False: return False
            return True
                
        blocks=[]
        for i in range(0,9,3):
            for j in range(0,9,3):
                blocks.append([board[i][j:j+3]+board[i+1][j:j+3]+board[i+2][j:j+3]])
        
        
        return (rowvalid(board) and colvalid(board) and squaresvalid(blocks))
        