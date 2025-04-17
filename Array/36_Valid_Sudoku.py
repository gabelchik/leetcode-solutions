class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}}
        for i in range(9):

            if i % 3 == 0:
                cubs = {0: {}, 1: {}, 2: {}}
            rows = {}

            for j in range(9):
                if board[i][j] != '.':
                    if (rows.get(board[i][j]) is None and cols[j].get(board[i][j]) is None
                    and cubs[j // 3].get(board[i][j]) is None):
                        rows[board[i][j]] = 1
                        cols[j][board[i][j]] = 1
                        cubs[j // 3][board[i][j]] = 1
                    else:
                        return False

        return True
