

def movezeros(arr):
    size = len(arr)
    if size < 2 : return arr
    l = 0
    for i in range(1, size):
        if arr[l] == 0:
            if arr[i] != 0:
                arr[l], arr[i] = arr[i], arr[l]
                l += 1
        else:
            l += 1
    print arr

arr = [0, 1, 0, 3, 12]

movezeros(arr)

