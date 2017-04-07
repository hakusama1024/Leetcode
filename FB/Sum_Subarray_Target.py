def sum_of_subarray_with_target(arr, target):
    dic = {}
    su = 0
    for i in range(len(arr)):
        su += arr[i]
        if su == target:
            print "0 to ", i
            break
        elif su - target in dic:
            print dic[su - target], " to ", i
            break
        else:
            dic[su] = i

arr = [2, 4, 2, 1, 5, -1, -8]

sum_of_subarray_with_target(arr, 7)
