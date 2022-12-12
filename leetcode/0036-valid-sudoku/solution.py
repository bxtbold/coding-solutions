class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        RUNTIME: 99 ms (92.26%)
        MEMORY: 13.8 MB (83.21%)
        """
        row, column, block = {}, {}, {}
        for i in range(9):
            row[i] = [k for k in board[i] if k != '.']
            if len(row[i]) != len(set(row[i])):
                return False
            for j in range(9):
                key = (i // 3) * 3 + j // 3
                if key not in block:
                    block[key] = []
                if j not in column:
                    column[j] = []
                if board[i][j] != '.':
                    if board[i][j] in block[key] or board[i][j] in column[j]:
                        return False
                    block[key].append(board[i][j])
                    column[j].append(board[i][j])
        return True
