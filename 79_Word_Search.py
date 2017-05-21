def word_search(arr, word):
    m = len(arr)
    if m == 0 : return False
    n = len(arr[0])
    for i in range(m):
        for j in range(n):
            if arr[i][j] == word[0]:



def helper(board, a, b, po, word):
    if po == len(word):
        return True
    if 0 <= a < len(board) and 0 <= b < len(board[0]):
        if board[a][b] == word[po]:
            res = self.helper(board, a+1, b, po+1, word) or self.helper(board, a, b+1, po+1, word) or helper(board, a-1, b, po+1, word)



arr = ["ABCE","SFCS","ADEE"]
word = "ABCCED"

word_search(arr, word)
