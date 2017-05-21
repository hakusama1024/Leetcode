def Sentence_Screen_Fitting(r, c, arr):
    if r == 0 or c == 0 : return ""


    index = 0
    total = 0

    for i in range(r):
        t = 0
        rem = c
        while len(arr[index]) <= rem:
            rem -= len(arr[index])
            t += len(arr[index])
            index += 1
            if index == len(arr) : 
                index = 0
                total += 1
            if t < c:
                t += 1
                rem -= 1
    print total

arr = ["hello", "world"]
arr = ["a", "bcd", "e"]
arr = ["I", "had", "apple", "pie"]

arr = ["try","to","be","better"]


Sentence_Screen_Fitting(10000, 9001, arr)

    




