class Solution(object):
    def updateBoard(self, board, click):
        if board[click[0]][click[1]] == "M": #지뢰밟고 겜종료
            board[click[0]][click[1]] = "X"
            return board

        lenXofBoard = len(board)
        lenYofBoard = len(board[0]) 

        marked = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]
        stack = []
        stack.append(click)
        while stack:
            #print(stack)
            now = stack.pop()
            x = now[0]
            y = now[1]

            tmp = []
            numNeighborBomb = 0

            for i in range(8):
                newX = x+dx[i]
                newY = y+dy[i]
                if 0 >newX or newX>=lenXofBoard or 0> newY or newY>=lenYofBoard:
                    continue
                if board[newX][newY] =="M":
                    numNeighborBomb+=1
                else:
                    if marked[newX][newY] ==False:
                        tmp.append([newX,newY])

            if numNeighborBomb ==0:
                board[x][y] = "B"
                stack = stack+tmp
                for x in tmp:
                    marked[x[0]][x[1]] = True
            else:
                board[x][y] =str(numNeighborBomb) 
        return board



        
