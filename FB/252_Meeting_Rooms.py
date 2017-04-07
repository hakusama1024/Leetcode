def meetingroom(arr):
    size =  len(arr)
    if size == 0 : return True
    arr.sort(key=lambda x: (x[0], x[1]))

    for i in range(1, size):
        if arr[i][0] < arr[i-1][1]:
            return False
    return True

def meetingroomII(arr):
    size = len(arr)
    if size == 0 : return 0
    start = []
    end = []
    for i in range(size):
        start.append(arr[i][0])
        end.append(arr[i][1])
    start.sort()
    end.sort()
    s = e = 0
    ava = room = 0
    while s < size:
        if start[s] < end[e]:
            if ava == 0 :
                room += 1
            else:
                ava -= 1
            s += 1
        else:
            ava +=1 
            e += 1
    return room

arr = [[0, 10],[5, 10],[15, 20]]






print meetingroom(arr)
print meetingroomII(arr)
