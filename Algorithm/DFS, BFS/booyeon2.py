class Solution(object):

    def __init__(self):
        # [y,x] 주위 탐색을 위한 방향값
        self.walkDir = [
            [1, -1], [1, 0], [1, 1],
            [0, -1],     [0, 1],
            [-1, -1], [-1, 0], [-1, 1]
        ]

    # ==========
    #  sub function
    # ==========
    '''
    :input: list[][] board, list[2] click ([y,x]형태)
    :output: str (현재 click위치에 입력할 상태값(결과값))(주위에 있는 mine의 갯수 or B(blank))

    :설명: 현재 click위치의 주위에 인접한 지뢰가 있는지 확인하여
        '{지뢰의 갯수}' or 없다면 'B' 를 return
    '''
    def checkMine(self, board, click):
        adjMine = 0  # 인접한 지뢰 수
        for d in self.walkDir:
            point = [click[0]+d[0], click[1]+d[1]]  # 현재확인할 위치
            # board 범위를 넘는지 확인
            if (point[0] < 0 or point[1] < 0) or \
                    (len(board) <= point[0] or len(board[0]) <= point[1]):
                continue

            if board[point[0]][point[1]] == 'M':  # 인접 지뢰 갯수 counting
                adjMine += 1

        # 갯수를 str로 return 없다면, 'B'
        return str(adjMine) if adjMine != 0 else 'B'

    # =============
    #  main function
    # =============
    """
        :input: :input: list[][] board, list[2] click ([y,x]형태)
        :output: list[][] board (현재 click위치에 대한 상태값이 변경된 board)

        :설명: board의 값을 탐색하여 click에 대한 적절한 board의 상태값을 return하는 함수
            dfs방식 사용
    """
    def updateBoard(self, board, click):

        if (board[click[0]][click[1]] == 'M'):  # click지접이 지뢰
            status = 'X'
        else:
            status = self.checkMine(board, click)  # 현재 지점의 상태확인

        board[click[0]][click[1]] = status  # board update

        if status == 'B':  # 현재 위치가 숫자거나 지뢰가 아닐때 탐색을 이어감

            for d in self.walkDir:
                point = [click[0]+d[0], click[1]+d[1]]  # 탐색할 위치
                # board 범위를 넘는지 확인
                if (point[0] < 0 or point[1] < 0) or \
                        (len(board) <= point[0] or len(board[0]) <= point[1]):
                    continue

                if board[point[0]][point[1]] == 'E':  # 미탐색지역이라면 탐색진행
                    board = self.updateBoard(board, point)

        return board
