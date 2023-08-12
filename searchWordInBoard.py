from typing import List 

from collections import defaultdict

class Solution:
    def createBoardMark(self, m: int, n: int) -> List[List[int]]:
        mat = [[]]*m 
        for i in range(m):
            mat[i] = [0]*n
        return mat
    
    def exist0(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        entry_point = []
        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if c == word[0]:
                    entry_point.append((i, j))
        if len(entry_point) == 0:
            return False
        
        def search_board(pre_pos: List[int], board_mark: List[List[int]], w: int, rowNum: int, colNum: int) -> bool:
            if w == len(word):
                return True
            
            r, c = pre_pos
            for r2, c2 in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                if r2 < rowNum and r2>=0 and \
                   c2 < colNum and c2>=0 and \
                   board_mark[r2][c2] == 0 and \
                   board[r2][c2] == word[w]:
                    board_mark[r2][c2] = 1
                    if search_board([r2, c2], board_mark, w+1, rowNum, colNum):
                        return True
                    board_mark[r2][c2] = 0
            
            return False
        
        board_mark = self.createBoardMark(m, n)
        for r, c in entry_point:
            board_mark[r][c] = 1
            if search_board([r,c], board_mark, 1, m, n):
                return True
            board_mark[r][c] = 0
        
        return False
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        if len(word) == 1:
            for i, r in enumerate(board):
                for j, c in enumerate(r):
                    if c == word:
                        return True
            return False


        entry_point = []
        sub2dict = [None]*m
        for i, r in enumerate(board):
            sub2dict[i] = [None]*n
            for j, c in enumerate(r):
                sub2dict[i][j] = defaultdict(list)
                for (i2, j2) in [(i+1,j), (i-1, j), (i, j-1), (i, j+1)]:
                    if i2 >= 0 and i2 < m and \
                      j2 >= 0 and j2 < n:
                        ss = c + board[i2][j2]
                        if ss == word[:2]:
                            if len(word) == 2:
                                return True
                            else:
                                entry_point.append((i,j))
                        if len(word) > 2:
                            sub2dict[i][j][ss].append((i2, j2))

        if len(entry_point) == 0:
            return False
        
        # len(word) > 2
        visited = self.createBoardMark(m, n)
        for r, c in entry_point:
            w = 0
            e2 = sub2dict[r][c].get(word[w:w+2])
            # todo, loop e2 list
            visited[r][c] = 1
            while e2 is not None:
                if w+2 >= len(word):
                    return True
                w += 1
                r, c = e2 
                e2 = sub2dict[r][c].get(word[w:w+2])
        
        return False
    
sol = Solution()
board = [["b","b"],
         ["a","b"],
         ["b","a"]]
word = "a"
print(f"find word:{word} in board: {board}, {sol.exist(board, word)}")

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "AX"
print(f"find word:{word} in board: {board}, {sol.exist(board, word)}")

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "FC"
print(f"find word:{word} in board: {board}, {sol.exist(board, word)}")

board = [["A"]]
word = "A"
print(f"find word:{word} in board: {board}, {sol.exist(board, word)}")

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCCED"
print(f"find word:{word} in board: {board}, {sol.exist(board, word)}")

board = [["A","B","C","E"],
         ["S","C","C","S"],
         ["A","D","F","E"]]
word = "ABCCED"
print(f"find word:{word} in board: {board}, {sol.exist(board, word)}")

board = [["A","B","C","E"],
         ["S","C","C","E"],
         ["A","D","E","D"]]
word = "ABCCED"
print(f"find word:{word} in board: {board}, {sol.exist(board, word)}")

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCB"
print(f"find word:{word} in board: {board}, {sol.exist(board, word)}")
