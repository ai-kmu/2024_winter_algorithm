class Solution:


  def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
    i, j = click
    if board[i][j] == 'M':
      board[i][j] = 'X'

      return board

    dirs = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
            (0, 1), (1, -1), (1, 0), (1, 1))

    def getMinesCount(i: int, j: int) -> int:
        around_cnt = 0

        for dx, dy in dirs:
            x = i + dx
            y = j + dy
            if x < 0 or x == len(board) or y < 0 or y == len(board[0]):
                continue
            if board[x][y] == 'M':
                around_cnt += 1

        return around_cnt

    def dfs(i: int, j: int) -> None:
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]):
            return

        if board[i][j] != 'E':
            return

        around_cnt = getMinesCount(i, j)

        if around_cnt == 0:
            board[i][j] = 'B'
            for dx, dy in dirs:
                dfs(i + dx, j + dy)

        else:
            board[i][j] = str(around_cnt)

    dfs(i, j)

    return board
