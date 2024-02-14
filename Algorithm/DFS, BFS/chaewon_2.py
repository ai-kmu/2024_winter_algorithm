from collections import deque


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click

        if board[x][y] == "M":
            board[x][y] = "X"
            return board

        dx = [0, 1, 0, -1, 1, 1, -1, -1]
        dy = [1, 0, -1, 0, 1, -1, 1, -1]
        queue = deque([(x, y)])

        while True:
            while queue:
                tmp = deque()
                x, y = queue.popleft()
                if board[x][y] == "M" or board[x][y] != "E":
                    continue
                
                mine = 0
                for i in range(8):
                    new_x = x + dx[i]
                    new_y = y + dy[i]
                    if new_x < 0 or new_x >= len(board) or new_y < 0 or new_y >= len(board[0]):
                        continue
                    elif board[new_x][new_y] == "M":
                        mine += 1
                    tmp.append((new_x, new_y))

                if mine > 0:
                    board[x][y] = str(mine)
                    continue
                else:
                    queue += tmp
                
                board[x][y] = "B"
                
            return board
