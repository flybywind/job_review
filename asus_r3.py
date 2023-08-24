# input
# int[] of length is even number
# in-place shuffle int[] 
# eg:
# a1, a2, a3, b1, b2, b3
# a1, b1, a2, b2, a3, b3

# ==> o(nlog(n)) if length is 2^n
# a1, a2, b1, b2
# a1, a2, a3, a4, b1, b2, b3, b4
#    a1, b1, b2, b3, a2, a3, a4, b4
#    a1, b1, a2, a3, b2, b3, a4, b4
#    a1, b1, a2, b2, a3, b3, a4, b4 
def interleaving(arr):
    n = len(arr)
    half = n//2
    for k in range(1, half):
        # swap i, half+i-1
        i = k*2-1
        tmp = arr[i]
        arr[i] = arr[half+k-1]
        for j in range(i+1, half+k):
            tmp2 = arr[j]
            arr[j] = tmp 
            tmp = tmp2
    return arr

def interleaving2(arr):
    n = len(arr)
    if n == 2:
        return arr
    
    seg = n//4
    tmp = arr[seg:seg*2]
    arr[seg:seg*2] = arr[seg*2:seg*3]
    arr[seg*2:seg*3] = tmp 
    return interleaving2(arr[:n//2]) + interleaving2(arr[n//2:])

arr = [1,2,3,4, -1, -2, -3, -4]
print(f"{interleaving(arr)}")
arr = [x for x in range(10)] + [-x for x in range(10)]
print(f"{interleaving(arr)}")

arr = [x for x in range(4)] + [-x for x in range(4)]
print(f"opt: {interleaving2(arr)}")
arr = [x for x in range(8)] + [-x for x in range(8)]
print(f"opt: {interleaving2(arr)}")