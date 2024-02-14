import queue


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        dx = [-1, -1, 0, 1, 1, 1, 0, -1]
        dy = [0, 1, 1, 1, 0, -1, -1, -1]

        x = click[0]
        y = click[1]

        ox = [[0 for j in range(len(board[0]))] for i in range(len(board))]

        q = deque()

        # 현재 board 값이 "M"이면 "X"로 바꾸고 board return
        if board[x][y] == "M":
            board[x][y] = "X"
            return board

        q.append((x, y))
        print(ox)
        while q:
            cnt = 0
            x, y = q.popleft()
            print(x, y)
            ox[x][y] = 1

            if board[x][y] == "E":

                tmp_q = deque()

                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < len(board) and 0 <= ny < len(board[0]):

                        if board[nx][ny] == "M":
                            cnt += 1

                        if ox[nx][ny] == 0:
                            tmp_q.append((nx, ny))

                if cnt == 0:
                    board[x][y] = "B"
                    q.extend(tmp_q)

                else:
                    board[x][y] = str(cnt)

        return board
