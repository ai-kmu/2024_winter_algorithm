class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]]=='M':
            board[click[0]][click[1]]='X'
            return board
        
        queue = deque([click])
        visited = set(tuple(click))
        num_location = set()
        d = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
        
        while queue:
            x, y = queue.popleft()
            
            if (x, y) in num_location:
                continue
                
            mine = 0
            temp_queue = deque()
            
            for tx, ty in d:
                nx, ny = x + tx, y + ty
                
                if not(0 <= nx < len(board)) or not(0 <= ny < len(board[0])):
                    continue
                    
                if board[nx][ny] == 'M':
                    mine += 1
                
                if (nx, ny) not in visited and board[nx][ny] == 'E':
                    temp_queue.append([nx, ny])
                    
            if mine > 0:
                board[x][y] = str(mine)
                num_location.add((x, y))
            else:
                board[x][y] = 'B'
                for each in temp_queue:
                    visited.add((each[0], each[1]))
                queue += temp_queue
                    
        return board
        
            
        
