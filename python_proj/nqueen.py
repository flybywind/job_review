def nqueen(n, v=0):
    path = [0]*n
    sol = 0
    def _recur(p, left, right, middle):
        nonlocal sol
        bitmap = left | right | middle 
        if bitmap == (1<<n)-1:
            return
        left2 = left >> 1
        right2 = right << 1
        for i in range(n):
            if (bitmap & (1<<i)) == 0:
                path[p] = i
                if p==n-1:
                    sol += 1
                    if v > 0:
                        print(f"find solution{sol}:")
                        for i in range(n):
                            for j in range(n):
                                if path[i] == j:
                                    print(f" * ", end="")
                                else:
                                    print(f" 0 ", end="")
                            print()
                    continue
                if i-1 >= 0:
                    left2 |= (1<<(i-1))
                if i+1 < n:
                    right2 |= (1<<(i+1))
                _recur(p+1, left2, right2, middle | (1<<i))
    _recur(0, 0, 0, 0)