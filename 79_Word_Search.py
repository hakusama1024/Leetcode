def word_search(arr, word):
    m = len(arr)
    if m == 0 : return False
    n = len(arr[0])
    visit = [[False] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if arr[i][j] == word[0]:
                if helper(arr, visit, i, j, 0, word) : return True
    return False



def helper(board,visit, a, b, po, word):
    if po == len(word):
        return True
    if a < 0 or a == len(board) or b < 0 or b == len(board[0]) or visit[a][b]: return False
    if board[a][b] == word[po]:
        visit[a][b] = True
        res = False
        for i, j in [[0,1], [0,-1], [1,0], [-1,0]]:
            res |= helper(board, visit, a+i, b+j, po+1, word)
            if res : return True
        visit[a][b] = False 
    return False



arr = ["ABCE","SFCS","ADEE"]
for i in arr:
    print i
word = "ABCCED"

print word_search(arr, word)
