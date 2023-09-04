def nqueen(n, v=0):
    path = [0]*n
    sol = 0
    sol_array = []

    def _recur(p, left, right, middle):
        nonlocal sol, sol_array
        bitmap = left | right | middle
        if bitmap == (1 << n)-1:
            return
        for i in range(n):
            if (bitmap & (1 << i)) == 0:
                left2 = left >> 1
                right2 = right << 1
                path[p] = i
                if p == n-1:
                    sol += 1
                    if v > 0:
                        sol_str = [f"---- find solution{sol} ---"]
                        for i in range(n):
                            row = ["    "]
                            for j in range(n):
                                if path[i] == j:
                                    row.append("*")
                                else:
                                    row.append("0")
                            sol_str.append(" ".join(row))
                        sol_array.append("\n".join(sol_str))
                    continue
                if i-1 >= 0:
                    left2 |= (1 << (i-1))
                if i+1 < n:
                    right2 |= (1 << (i+1))
                _recur(p+1, left2, right2, middle | (1 << i))
    _recur(0, 0, 0, 0)
    return sol, sol_array
