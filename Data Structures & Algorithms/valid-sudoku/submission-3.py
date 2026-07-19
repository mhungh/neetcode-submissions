class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        sqrs = [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr == ".":
                    continue
                if curr not in rows[i]:
                    rows[i].add(curr)
                else:
                    return False
                if curr not in cols[j]:
                    cols[j].add(curr)
                else:
                    return False
                if curr not in sqrs[int(i/3)*3 + int(j/3)]:
                    sqrs[int(i/3)*3 + int(j/3)].add(curr)
                else:
                    return False
        return True
        