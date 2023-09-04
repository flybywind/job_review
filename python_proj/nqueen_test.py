from nqueen import nqueen


def testNQueen():
    for n in range(13):
        v = 1 if n < 7 else 0
        sol, ary = nqueen(n, v)
        sol_str = ""
        if len(ary) > 0:
            sol_str = "\n".join(ary)
        print(f"n = {n}, solution = {sol}, \n{sol_str}")


'''
n = 1, solution = 1, 
---- find solution1 ---
     *
n = 2, solution = 0, 

n = 3, solution = 0, 

n = 4, solution = 2, 
---- find solution1 ---
     0 * 0 0
     0 0 0 *
     * 0 0 0
     0 0 * 0
---- find solution2 ---
     0 0 * 0
     * 0 0 0
     0 0 0 *
     0 * 0 0
n = 5, solution = 10, 
---- find solution1 ---
     * 0 0 0 0
     0 0 * 0 0
     0 0 0 0 *
     0 * 0 0 0
     0 0 0 * 0
---- find solution2 ---
     * 0 0 0 0
     0 0 0 * 0
     0 * 0 0 0
     0 0 0 0 *
     0 0 * 0 0
---- find solution3 ---
     0 * 0 0 0
     0 0 0 * 0
     * 0 0 0 0
     0 0 * 0 0
     0 0 0 0 *
---- find solution4 ---
     0 * 0 0 0
     0 0 0 0 *
     0 0 * 0 0
     * 0 0 0 0
     0 0 0 * 0
---- find solution5 ---
     0 0 * 0 0
     * 0 0 0 0
     0 0 0 * 0
     0 * 0 0 0
     0 0 0 0 *
---- find solution6 ---
     0 0 * 0 0
     0 0 0 0 *
     0 * 0 0 0
     0 0 0 * 0
     * 0 0 0 0
---- find solution7 ---
     0 0 0 * 0
     * 0 0 0 0
     0 0 * 0 0
     0 0 0 0 *
     0 * 0 0 0
---- find solution8 ---
     0 0 0 * 0
     0 * 0 0 0
     0 0 0 0 *
     0 0 * 0 0
     * 0 0 0 0
---- find solution9 ---
     0 0 0 0 *
     0 * 0 0 0
     0 0 0 * 0
     * 0 0 0 0
     0 0 * 0 0
---- find solution10 ---
     0 0 0 0 *
     0 0 * 0 0
     * 0 0 0 0
     0 0 0 * 0
     0 * 0 0 0
n = 6, solution = 4, 
---- find solution1 ---
     0 * 0 0 0 0
     0 0 0 * 0 0
     0 0 0 0 0 *
     * 0 0 0 0 0
     0 0 * 0 0 0
     0 0 0 0 * 0
---- find solution2 ---
     0 0 * 0 0 0
     0 0 0 0 0 *
     0 * 0 0 0 0
     0 0 0 0 * 0
     * 0 0 0 0 0
     0 0 0 * 0 0
---- find solution3 ---
     0 0 0 * 0 0
     * 0 0 0 0 0
     0 0 0 0 * 0
     0 * 0 0 0 0
     0 0 0 0 0 *
     0 0 * 0 0 0
---- find solution4 ---
     0 0 0 0 * 0
     0 0 * 0 0 0
     * 0 0 0 0 0
     0 0 0 0 0 *
     0 0 0 * 0 0
     0 * 0 0 0 0
n = 7, solution = 40, 

n = 8, solution = 92, 

n = 9, solution = 352, 

n = 10, solution = 724, 

n = 11, solution = 2680, 

n = 12, solution = 14200, 
'''
