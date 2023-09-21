def findDup(arr) -> int:
    N = len(arr)
    idx = 0
    while idx < N:
        x = arr[idx]
        if x == idx:
            idx += 1
            continue
        # else
        tmp = arr[x]
        if tmp == x:  # already got a x in the right position
            return tmp
        arr[idx] = tmp
        arr[x] = x
