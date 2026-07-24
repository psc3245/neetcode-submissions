class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            if not self.check_nine(row):
                return False

        for i in range(9):
            col = []
            for j in range(9):
                col.append(board[j][i])
            if not self.check_nine(col):
                return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append(board[box_row + i][box_col + j])
                if not self.check_nine(box):
                    return False
        return True

        


    def check_nine(self, nine):
        s = set([])
        for n in nine:
            if n != ".":
                if n in s:
                    return False
                else:
                    s.add(n)
        return True