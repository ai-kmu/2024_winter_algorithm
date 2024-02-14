class Solution:
    # 주변에 mine이 있을경우 업데이트 해줘야하는 NumMines += 1
    def getAdjacentMines(self, board, x, y):
        numMines = 0
        for r in range(x-1, x+2):
            for c in range(y-1, y+2):
                if 0 <= r < len(board) and 0 <= c < len(board[r]) and board[r][c] == "M":
                    numMines += 1
        return numMines

    # 보드 업데이트
    def updateBoard(self, board, click):
        # 보드 없으면 그냥 반환
        if not board:
            return board
        x, y = click
        # Mine이면 X 반환
        if board[x][y] == 'M':
            board[x][y] = "X"
        # e를 클릭했을때
        else:
            numMines = self.getAdjacentMines(board, x, y)
            # 숫자로 채워야 하는 상황일때
            if numMines:
                board[x][y] = str(numMines)
            # B로 채워야 하는 상황일때
            else:
                board[x][y] = "B"
                for r in range(x-1, x+2):
                    for c in range(y-1, y+2):
                        if 0 <= r < len(board) and 0 <= c < len(board[r]) and board[r][c] != "B":
                            self.updateBoard(board, [r, c])
        return board
